def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_and_right(n):
    while n >= 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sorted([i for i in primes if truncate_left_and_right(i)], reverse=True)