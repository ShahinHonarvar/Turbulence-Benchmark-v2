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

def is_left_right_truncatable_prime(n):
    if '0' in str(n) or not is_prime(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        if str_n and (not is_prime(int(str_n))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[1]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)