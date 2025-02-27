def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 11:
            if not is_prime(n // 10) or not is_prime(n % 10):
                return False
            n //= 10
        return True
    x = numbers[70]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)