def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
    for i in range(len(n_str) - 1):
        if not is_prime(int(n_str[:-i - 1])):
            return False
    return True

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[975]
    truncable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncable_primes.append(i)
    return sorted(truncable_primes, reverse=True)