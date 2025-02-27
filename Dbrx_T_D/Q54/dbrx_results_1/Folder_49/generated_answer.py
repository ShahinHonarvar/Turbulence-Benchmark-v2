def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    while n > 9:
        n = int(str(n)[:-1])
    return n

def all_right_truncatable_prime(n):
    x = n[13]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        curr = prime
        while curr > 0:
            if is_prime(curr):
                right_truncatable_primes.append(curr)
            curr = remove_last_digit(curr)
    return sorted(list(set(right_truncatable_primes)))