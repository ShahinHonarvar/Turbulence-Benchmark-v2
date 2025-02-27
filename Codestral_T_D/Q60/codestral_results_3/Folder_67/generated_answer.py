def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
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
        if '0' in str(n):
            return False
        num = n
        while num >= 10:
            num = truncate_left(num)
            if not is_prime(num):
                return False
        num = n
        while num >= 10:
            num = truncate_right(num)
            if not is_prime(num):
                return False
        return True
    for i in range(x, 1, -1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result