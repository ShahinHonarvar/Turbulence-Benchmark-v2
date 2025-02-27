def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, primes):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[-i:])) or int(s[-i:]) not in primes:
                return False
        return True
    x = t[758]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_truncatable(i, primes)])