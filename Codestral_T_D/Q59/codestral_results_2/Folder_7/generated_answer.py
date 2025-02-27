def all_left_truncatable_prime(t):
    x = t[803]
    primes = [2]
    left_truncatable_primes = []
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            str_i = str(i)
            if '0' not in str_i and all((int(str_i[j:]) in primes for j in range(1, len(str_i)))):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)