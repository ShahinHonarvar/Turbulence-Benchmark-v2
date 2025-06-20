def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:-i])
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[14]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)