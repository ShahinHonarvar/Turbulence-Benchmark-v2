def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate(n):
    return [int(str(n)[i:j]) for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)]

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i) and (not '0' in str(i))]
    return [i for i in primes if all((x in primes for x in truncate(i)))]