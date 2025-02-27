def all_right_truncatable_prime(t):
    x = t[79]
    primes = []
    for i in range(x, 0, -1):
        s = str(i)
        is_prime = True
        for j in range(len(s)):
            n = int(s[0:len(s) - j])
            if n < 2:
                is_prime = False
                break
            for k in range(2, int(n ** 0.5) + 1):
                if n % k == 0:
                    is_prime = False
                    break
            if not is_prime:
                break
        if is_prime:
            primes.append(i)
    return sorted(primes, reverse=True)