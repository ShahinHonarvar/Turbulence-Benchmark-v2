def all_left_truncatable_prime(t):
    x = t[1]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
    ltp = []
    for p in primes:
        if len(str(p)) == 1:
            ltp.append(p)
        else:
            left_trimmed = int(str(p)[1:])
            if left_trimmed in primes and all((int(str(p)[i:] + str(left_trimmed)) in primes for i in range(1, len(str(p))))):
                ltp.append(p)
    ltp.sort(reverse=True)
    return ltp