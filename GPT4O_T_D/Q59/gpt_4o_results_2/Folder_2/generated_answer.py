def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 618:
        return []
    x = numbers[618]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes