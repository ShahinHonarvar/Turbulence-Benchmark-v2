def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)