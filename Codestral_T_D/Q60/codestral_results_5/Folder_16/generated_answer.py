def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    result = []

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
        while n > 0:
            n = truncate_left(n)
            if n == 0:
                break
            if not is_prime(n):
                return False
        n = numbers[792]
        while n > 0:
            n = truncate_right(n)
            if n == 0:
                break
            if not is_prime(n):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)