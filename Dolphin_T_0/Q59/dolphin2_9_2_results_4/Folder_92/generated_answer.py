def all_left_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
        else:
            continue
    left_truncatable = [p for p in primes if all((int(str(p)[i:]) in primes for i in range(len(str(p)))))]
    return sorted(left_truncatable)