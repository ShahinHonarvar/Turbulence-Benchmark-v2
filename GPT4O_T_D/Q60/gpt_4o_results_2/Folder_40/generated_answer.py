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

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        s = s[1:-1]
        if s and (not is_prime(int(s))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 10:
        return []
    x = numbers[10]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)