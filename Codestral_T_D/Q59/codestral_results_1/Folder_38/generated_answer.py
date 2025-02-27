def all_left_truncatable_prime(t):
    x = t[28]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    ltp_primes = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            ltp = True
            for i in range(1, len(str_p)):
                if int(str_p[i:]) not in primes:
                    ltp = False
                    break
            if ltp:
                ltp_primes.append(p)
    return sorted(ltp_primes)