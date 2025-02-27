def all_right_truncatable_prime(t):
    x = t[77]

    def isprime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def righttruncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    result = []
    for i in range(x):
        if isprime(i) and righttruncatable(i):
            result.append(i)
    return sorted(result)