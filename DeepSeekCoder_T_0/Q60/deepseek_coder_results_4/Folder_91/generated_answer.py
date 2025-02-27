def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_truncatable_primes(limit):
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    while primes:
        prime = primes.pop(0)
        if prime > limit:
            continue
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        if all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:len(str_prime) - i])) for i in range(len(str_prime)))):
            truncatable_primes.append(prime)
        next_primes = [int(str_prime + str(d)) for d in range(1, 10) if is_prime(int(str_prime + str(d)))]
        primes.extend(next_primes)
    return truncatable_primes

def all_left_right_truncatable_prime(t):
    limit = t[0]
    truncatable_primes = generate_truncatable_primes(limit)
    return sorted(truncatable_primes, reverse=True)