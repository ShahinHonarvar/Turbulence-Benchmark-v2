def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_number(n):
    while n > 9:
        n //= 10
    return n

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        if str(prime)[0] in ('1', '2', '3', '5', '7') and is_prime(prime) and is_prime(truncate_number(prime)):
            left_right_truncatable_primes.append(prime)
    return sorted(list(set(left_right_truncatable_primes)))