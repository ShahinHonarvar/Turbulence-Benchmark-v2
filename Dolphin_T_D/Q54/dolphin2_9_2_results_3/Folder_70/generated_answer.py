def all_right_truncatable_prime(t):
    x = t[433]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            if i in primes:
                for _ in range(len(str(i)) - 1):
                    i = int(str(i)[1:])
                    if i in primes:
                        pass
                    else:
                        break
                else:
                    primes.append(i)
    primes.sort(reverse=True)
    return primes