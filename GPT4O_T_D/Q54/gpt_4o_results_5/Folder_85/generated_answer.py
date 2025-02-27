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

def right_truncatable(prime):
    s = str(prime)
    for i in range(len(s), 0, -1):
        if not is_prime(int(s[:i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 95:
        return []
    x = numbers[94]
    right_truncatable_primes = []
    for number in range(2, x):
        if is_prime(number) and right_truncatable(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)