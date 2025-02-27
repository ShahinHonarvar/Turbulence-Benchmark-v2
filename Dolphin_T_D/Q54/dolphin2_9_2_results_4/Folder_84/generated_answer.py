def all_right_truncatable_prime(t):

    def is_prime(n):
        if n:
            if n % 2:
                i = 3
                while i < n and n % i:
                    i += 2
                else:
                    return False
        return True

    def is_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(0, len(str(n)))))
    x = t[630]
    primes = [n for n in range(2, x) if is_prime(n) and is_truncatable(n)]
    return sorted(primes, reverse=True) or []