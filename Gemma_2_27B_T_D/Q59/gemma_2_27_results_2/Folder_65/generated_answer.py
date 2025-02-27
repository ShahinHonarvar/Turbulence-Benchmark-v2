def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[32]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            s = str(i)
            is_truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)