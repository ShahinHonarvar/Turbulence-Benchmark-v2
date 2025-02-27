def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(num):
    x = num[96]
    primes = [i for i in range(x, 0, -1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if prime < 10:
            truncatable_primes.append(prime)
        else:
            for digit in range(10, 0, -1):
                q = prime // digit
                r = prime % digit
                if r == 0 and q in truncatable_primes:
                    truncatable_primes.append(prime)
                    break
    return truncatable_primes