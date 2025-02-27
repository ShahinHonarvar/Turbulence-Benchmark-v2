def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[38]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        num = prime
        while len(str(num)) > 1:
            if num not in primes or not is_prime(int(str(num)[1:])):
                break
            num = int(str(num)[1:])
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)