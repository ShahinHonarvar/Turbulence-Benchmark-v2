def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[:-1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 33:
        return []
    x = numbers[33]
    truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)