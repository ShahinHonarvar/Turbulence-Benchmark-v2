import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[803]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)