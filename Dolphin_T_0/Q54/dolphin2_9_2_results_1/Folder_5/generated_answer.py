def all_right_truncatable_prime(t):
    x = t[55]
    primes = [2, 3, 5, 7]
    i = 10
    while i < x:
        if i % 10 in {2, 3, 5, 7}:
            if all((i % n != 0 for n in primes)):
                if i > 10:
                    if all((i % n != 0 for n in primes)):
                        primes.append(i)
            i += 10
        else:
            i += 1
    primes.sort()
    return primes