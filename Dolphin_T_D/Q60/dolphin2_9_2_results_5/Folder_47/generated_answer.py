def all_left_right_truncatable_prime(n):
    x = n[49]
    primes = [2]
    for possible_prime in range(3, x + 1):
        for p in primes:
            if possible_prime % p == 0:
                break
        else:
            primes.append(possible_prime)
    return [p for p in primes if str(p).count('0') == 0 and all((int(str(p)[i:j]) in primes for i in range(1, len(str(p))) for j in range(i + 1, len(str(p)) + 1)))]