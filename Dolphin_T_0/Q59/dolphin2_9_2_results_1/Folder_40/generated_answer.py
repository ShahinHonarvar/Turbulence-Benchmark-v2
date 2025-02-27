def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[10]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatables = []
    for p in primes:
        s = str(p)
        while len(s) > 0 and is_prime(int(s)):
            left_truncatables.append(int(s))
            s = s[1:]
    return sorted(list(set(left_truncatables)), reverse=True)