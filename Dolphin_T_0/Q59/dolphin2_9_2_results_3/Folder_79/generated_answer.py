def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[91]
    primes = []
    for i in range(2, x):
        s = str(i)
        if '0' not in s:
            prime = True
            for j in range(0, len(s) - 1):
                if not is_prime(int(s[j:])):
                    prime = False
                    break
            if prime:
                primes.append(i)
    return sorted(primes)