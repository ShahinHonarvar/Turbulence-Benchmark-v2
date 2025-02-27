def all_right_truncatable_prime(t):
    x = t[19]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for d in reversed(str(n)):
            if not is_prime(int(d)):
                return False
            n = n // 10
        return True
    result = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(result) or []