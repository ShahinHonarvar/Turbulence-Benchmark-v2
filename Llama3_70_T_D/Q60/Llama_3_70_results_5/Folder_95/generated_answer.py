def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[77]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            is_truncatable = True
            for i in range(1, len(str_prime)):
                if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)