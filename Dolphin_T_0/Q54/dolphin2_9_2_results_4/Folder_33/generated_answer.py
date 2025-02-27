def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if is_prime(n):
        last_digit = n % 10
        if last_digit != 0:
            return is_truncatable(n // 10)
    return False

def all_right_truncatable_prime(param):
    x = param[945]
    primes = [i for i in range(x) if is_truncatable(i)]
    return sorted(primes, reverse=True)