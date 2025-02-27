def all_right_truncatable_prime(t):
    x = t[24]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            num = str(i)
            for j in range(1, len(num)):
                if int(num[:-j]) % 2 == 0 or int(num[:-j]) % 3 == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes)