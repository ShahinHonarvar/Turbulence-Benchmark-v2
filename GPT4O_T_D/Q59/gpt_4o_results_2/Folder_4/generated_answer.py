def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    while len(str_n) > 0:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(tpl):
    x = tpl[96]
    left_truncatable_primes = []
    for number in range(2, x):
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)