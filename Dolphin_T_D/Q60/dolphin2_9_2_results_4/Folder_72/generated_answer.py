def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_and_right_truncation(n):
    n = str(n)
    for _ in range(1, len(n) - 1):
        n = n[1:-1]
        if not is_prime(int(n)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[31]
    primes_list = [i for i in range(2, x + 1) if is_prime(i)]
    primes_list = [i for i in primes_list if left_and_right_truncation(i)]
    return sorted(primes_list, reverse=True) if primes_list else []