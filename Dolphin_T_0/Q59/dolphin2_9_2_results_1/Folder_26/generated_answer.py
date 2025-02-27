def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0 and n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[81]
    primes = [i for i in range(2, x) if is_prime(i) and n[::-1] not in str(i) for n in str(i)]
    return sorted([p for p in primes if is_left_truncatable_prime(p)], reverse=True)