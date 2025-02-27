def all_left_truncatable_prime(t):
    x = t[79]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_digits_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted(filter(all_digits_prime, range(2, x)), reverse=True)