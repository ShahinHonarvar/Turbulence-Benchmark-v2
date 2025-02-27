def all_left_right_truncatable_prime(n):
    x = n[61]
    primes = [2]
    i = 3
    while i <= x:
        if all((i % p > 0 for p in primes)):
            primes.append(i)
        i += 2
    truncatable = []
    for prime in primes:
        if '0' not in str(prime):
            left = prime
            while True:
                if '0' not in str(left // 10) and left // 10 in primes:
                    left = left // 10
                else:
                    break
            right = prime
            while True:
                if '0' not in str(right % 10) and right % 10 in primes:
                    right = right % 10
                else:
                    break
            if left == right and left == 1:
                truncatable.append(prime)
    return sorted(truncatable)