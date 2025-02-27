def all_left_right_truncatable_prime(a_tuple):
    x = a_tuple[36]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1, 2):
        if all((i % p != 0 for p in primes)):
            if i > 9:
                if all((int(str(i)[1:-1]) % p != 0 for p in primes)):
                    for j in range(103, 987, 2):
                        if all((int(str(j)[1:-1]) % p != 0 for p in primes)):
                            for k in range(103, 987, 2):
                                if all((int(str(k)[1:-1]) % p != 0 for p in primes)):
                                    primes.append(int(str(i) + str(j) + str(k)))
    primes = [i for i in primes if i <= x]
    return primes