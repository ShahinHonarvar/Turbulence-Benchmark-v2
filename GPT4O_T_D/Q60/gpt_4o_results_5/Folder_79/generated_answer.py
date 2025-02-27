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

def is_left_right_truncatable(prime):
    s = str(prime)
    while len(s) > 2:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return len(s) == 1 or is_prime(int(s))

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 91:
        return []
    x = numbers[91]
    truncatable_primes = []
    for n in range(10, x + 1):
        if '0' not in str(n) and is_prime(n):
            if is_left_right_truncatable(n):
                truncatable_primes.append(n)
    return truncatable_primes