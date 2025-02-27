def all_left_truncatable_prime(p):
    x = p[43]
    result = []

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(n):
        if n == 0 or n % 10 == 0:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for n in range(10, x):
        if is_truncatable_prime(n):
            result.append(n)
    return sorted(result)