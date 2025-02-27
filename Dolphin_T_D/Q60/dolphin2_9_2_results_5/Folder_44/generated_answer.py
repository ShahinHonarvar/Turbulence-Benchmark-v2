def all_left_right_truncatable_prime(t):
    x = t[39]
    primes = [2]
    if x < 2:
        return []
    i = 3
    while i * i <= x:
        if all((i % p > 0 for p in primes)):
            primes.append(i)
        i += 2
    primes = [p for p in primes if p <= x and all((str.count(d) == 0 for d in '0'))]
    left_right_truncatable_primes = []
    for prime in primes:
        if len(str(prime)) > 3:
            left_truncation = str(prime)[1:-1]
            right_truncation = str(prime)[0:-2]
            if set(left_truncation).issubset(set(str(123456789))) and set(right_truncation).issubset(set(str(123456789))) and (int(left_truncation) in primes) and (int(right_truncation) in primes):
                left_right_truncatable_primes.append(prime)
    return left_right_truncatable_primes