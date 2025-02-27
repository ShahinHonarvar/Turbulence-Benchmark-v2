def all_left_right_truncatable_prime(t):

    def is_truncatable(n):
        if n < 2 or '0' in str(n):
            return False
        while n > 0:
            if str(n) not in primes:
                return False
            n = int(str(n)[1:]) if n > 10 else 0
        return True
    x = t[100]
    primes = [str(p) for p in range(2, x + 1) if all((p % i for i in range(2, int(p ** 0.5) + 1)))]
    return sorted([int(p) for p in primes if is_truncatable(int(p))], reverse=True)