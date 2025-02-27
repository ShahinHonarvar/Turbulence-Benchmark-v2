def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
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
    str_n = str(n)
    length = len(str_n)
    if '0' in str_n:
        return False
    for i in range(length):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:length - i])
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)