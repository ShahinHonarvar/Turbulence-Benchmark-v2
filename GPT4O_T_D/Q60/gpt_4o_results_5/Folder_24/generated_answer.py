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

def left_right_truncatable(prime):
    s = str(prime)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[1:] if len(s) > 1 else ''
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 66:
        return []
    x = numbers[65]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and left_right_truncatable(num) and left_right_truncatable(str(num)[::-1]):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes