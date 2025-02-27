def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = t[36]
    primes = [n for n in range(2, x) if is_prime(n)]
    return sorted([p for p in primes if all((is_prime(int(str(p)[i:])) for i in range(len(str(p)))))], reverse=True)