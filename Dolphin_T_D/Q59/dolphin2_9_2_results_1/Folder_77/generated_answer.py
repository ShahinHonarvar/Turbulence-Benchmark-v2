def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[767]
    left_truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            s = str(i)
            while s:
                if not is_prime(int(s)):
                    break
                s = s[1:]
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)