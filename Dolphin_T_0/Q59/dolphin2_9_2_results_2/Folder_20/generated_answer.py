def all_left_truncatable_prime(t):

    def is_prime(n):
        if n and n % 2:
            i = 3
            while i * i <= n:
                if n % i:
                    i += 2
                else:
                    return False
            return True
        return False

    def is_truncatable(s):
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[100]
    primes = [p for p in range(7, x, 2) if is_prime(p) and is_truncatable(str(p))]
    primes.sort(reverse=True)
    return primes