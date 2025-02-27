def all_right_truncatable_prime(t):
    x = t[630]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        isPrime = True
        for j in range(len(s)):
            n = int(s[:len(s) - j])
            if n < 2:
                isPrime = False
                break
            for k in range(2, int(n ** 0.5) + 1):
                if n % k == 0:
                    isPrime = False
                    break
            if not isPrime:
                break
        if isPrime:
            primes.append(i)
    return sorted(primes, reverse=True)