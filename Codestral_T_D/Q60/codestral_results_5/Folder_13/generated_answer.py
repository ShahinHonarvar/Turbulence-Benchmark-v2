def all_left_right_truncatable_prime(numbers):

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

    def truncate_both(n):
        return truncate_left(n) if truncate_left(n) < 10 else truncate_right(n)

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = truncate_both(n)
            if not is_prime(n):
                return False
        return True
    x = numbers[784]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result