def all_right_truncatable_prime(t):
    x = t[93]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[:j]) in primes for j in range(1, len(str(i))))):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
    return sorted(primes)