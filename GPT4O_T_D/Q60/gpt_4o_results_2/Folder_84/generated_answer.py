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

def is_truncatable_prime(prime):
    s = str(prime)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    s = str(prime)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 630:
        return []
    x = numbers[630]
    truncatable_primes = []
    for number in range(11, x + 1):
        if '0' in str(number):
            continue
        if is_prime(number) and is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)