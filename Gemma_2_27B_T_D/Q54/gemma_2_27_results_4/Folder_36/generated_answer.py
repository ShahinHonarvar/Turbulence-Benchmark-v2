def all_right_truncatable_prime(t):
    x = t[992]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(1, x):
        s = str(i)
        flag = True
        while len(s) > 0:
            if not is_prime(int(s)):
                flag = False
                break
            s = s[:-1]
        if flag:
            primes.append(i)
    primes.sort()
    return primes