def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(p):
    if len(str(p)) <= 2:
        return True
    return is_prime(int(str(p)[1:])) and is_truncanble(int(str(p)[:-1]))

def all_left_right_truncatable_prime(t):
    x = t[618]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable = [i for i in primes if is_truncatable(i)]
    return sorted(truncatable)