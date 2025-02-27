def all_left_truncatable_prime(tup):
    x = tup[33]
    primes = [2]
    for n in range(3, x):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
    left_truncatable = []
    for prime in primes:
        str_num = str(prime)
        if '0' in str_num:
            continue
        else:
            for i in range(len(str_num)):
                if int(str_num[i:]) not in primes:
                    break
            else:
                left_truncatable.append(prime)
    left_truncatable.sort()
    return left_truncatable