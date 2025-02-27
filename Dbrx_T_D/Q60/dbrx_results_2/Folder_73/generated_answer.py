def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_left_digit(n):
    return int(str(n)[1:])

def remove_right_digit(n):
    return int(str(n)[:-1])

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = remove_left_digit(n)
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = remove_right_digit(n)
    return True

def is_left_and_right_truncatable_prime(n):
    return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)

def all_left_right_truncatable_prime(t):
    x = 97
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    l_r_trunc_primes = [i for i in primes if is_left_and_right_truncatable_prime(i)]
    return l_r_trunc_primes