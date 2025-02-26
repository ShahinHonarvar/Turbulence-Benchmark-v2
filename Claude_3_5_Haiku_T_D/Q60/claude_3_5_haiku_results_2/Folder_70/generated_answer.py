def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        if n < 10:
            break
        n_str = str(n)
        n = int(n_str[1:] if len(n_str) > 1 else 0)
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[433]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes