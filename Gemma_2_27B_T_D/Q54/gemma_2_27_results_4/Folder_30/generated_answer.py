def all_right_truncatable_prime(t):
    x = t[37]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        s = str(i)
        flag = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                flag = False
                break
        if flag:
            primes.append(i)
    return sorted(primes, reverse=True)