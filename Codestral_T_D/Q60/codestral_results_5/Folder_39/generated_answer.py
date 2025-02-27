def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = truncate_left(temp)
            if temp < 10:
                break
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = truncate_right(temp)
            if temp < 10:
                break
        return True
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)