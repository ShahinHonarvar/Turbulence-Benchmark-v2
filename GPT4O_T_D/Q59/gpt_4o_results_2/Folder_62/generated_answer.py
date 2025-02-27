def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 70:
        return []
    x = numbers[70]
    truncatable_primes = []
    for n in range(2, x):
        if '0' not in str(n) and left_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes