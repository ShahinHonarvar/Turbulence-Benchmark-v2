def all_left_truncatable_prime(t):
    x = t[32]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        for p in primes:
            if num % p == 0:
                break
        else:
            sNum = str(num)
            if '0' not in sNum:
                trunc = sNum
                while True:
                    if len(trunc) == 1:
                        primes.append(int(trunc))
                        break
                    if int(trunc) in primes:
                        trunc = trunc[1:]
                    else:
                        break
    primes.sort()
    return primes