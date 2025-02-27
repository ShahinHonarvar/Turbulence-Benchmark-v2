def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_right(n):
    while n > 9:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    while n > 9:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return is_prime(n)

def all_left_right_truncatable_prime(tup):
    x = tup[38]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_primes = [i for i in primes if truncate_left_right(i)]
    left_right_primes.sort(reverse=True)
    return left_right_primes