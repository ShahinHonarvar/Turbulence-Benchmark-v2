def all_left_truncatable_prime(t):
    x = t[176]
    primes = [p for p in range(x) if all(str(p) not in '0' and all((abs(p - int(s)) >= 2 for s in str(p))))]
    left_truncatable_primes = []
    for p in primes:
        if all((str(p)[:len(str(q)) - 1] in primes for q in primes if q > p)):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)