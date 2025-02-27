def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(n, direction='left'):
        if direction == 'left':
            return int(str(n)[1:])
        else:
            return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        for i in range(len(str(n)) - 1):
            n = truncate(n)
            if not is_prime(n) or '0' in str(n):
                return False
            n = truncate(n, 'right')
            if not is_prime(n) or '0' in str(n):
                return False
        return True
    x = numbers[618]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])