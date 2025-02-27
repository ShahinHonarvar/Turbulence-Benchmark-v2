def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[1]
    list_of_primes = [i for i in range(x, 0, -1) if is_right_truncatable_prime(i)]
    return sorted(list_of_primes, reverse=True)