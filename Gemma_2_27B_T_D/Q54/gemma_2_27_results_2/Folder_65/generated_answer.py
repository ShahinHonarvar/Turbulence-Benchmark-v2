def all_right_truncatable_prime(t):
    x = t[32]
    primes = []
    for num in range(2, x):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    truncatable = []
    for num in primes:
        truncatable_prime = True
        n = str(num)
        while len(n) > 0:
            if int(n) not in primes:
                truncatable_prime = False
                break
            n = n[:-1]
        if truncatable_prime:
            truncatable.append(num)
    truncatable.sort()
    return truncatable