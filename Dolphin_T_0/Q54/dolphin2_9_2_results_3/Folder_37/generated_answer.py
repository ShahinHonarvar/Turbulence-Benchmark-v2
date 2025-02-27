def all_right_truncatable_prime(t):
    x = t[35]

    def is_right_truncatable_prime(n):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            while n > 0:
                if not all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
                    return False
                n //= 10
            return True
        return False
    return sorted([i for i in range(2, x) if is_right_truncutable_prime(i)], reverse=True)