def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            left_trunc = int(n[i:])
            right_trunc = int(n[:-i or None])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = numbers[23]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)])