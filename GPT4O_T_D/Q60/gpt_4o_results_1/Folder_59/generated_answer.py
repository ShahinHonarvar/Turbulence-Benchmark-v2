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

def is_truncatable(prime):
    str_prime = str(prime)
    length = len(str_prime)
    if '0' in str_prime:
        return False
    for i in range(1, length):
        left_truncate = int(str_prime[i:])
        right_truncate = int(str_prime[:length - i])
        if not (is_prime(left_truncate) and is_prime(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 84:
        return []
    x = numbers[84]
    left_right_truncatable_primes = []
    for i in range(11, x + 1):
        if is_prime(i) and is_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes, reverse=True)