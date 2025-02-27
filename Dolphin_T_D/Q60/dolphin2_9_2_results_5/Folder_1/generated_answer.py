def all_left_right_truncatable_prime(p):
    x = p[20]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, i)))]
    left_right_truncatable_primes = []
    for p in primes:
        if set(str(p)) == {'1', '3', '7', '9'} and len(str(p)) >= 2:
            for i in range(1, len(str(p)) - 1):
                if int(str(p)[i:]) not in primes or int(str(p)[:-i]) not in primes:
                    break
            else:
                left_right_truncatable_primes.append(p)
    return sorted(left_right_truncatable_primes, reverse=True)