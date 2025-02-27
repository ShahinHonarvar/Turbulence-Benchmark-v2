def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_righ_truncatable = [p for p in primes if str(p).count('0') == 0 and len(str(p)) >= 2 and all(is_prime(int(str(p)[1:-1]))) and all((is_prime(int(str(p)[i:-(i + 1)])) for i in range(1, len(str(p)) - 1)))]
    left_righ_truncatable.sort()
    return left_righ_truncatable