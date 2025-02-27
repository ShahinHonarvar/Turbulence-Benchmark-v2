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

def is_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    length = len(str_n)
    for i in range(length):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:length - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 29:
        return []
    x = numbers[28]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes