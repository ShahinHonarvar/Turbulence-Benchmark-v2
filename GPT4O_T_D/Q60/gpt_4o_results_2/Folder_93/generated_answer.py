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

def truncatable_primes(n):
    s = str(n)
    for i in range(1, len(s)):
        if not (is_prime(int(s[i:])) and is_prime(int(s[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    result = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i) and truncatable_primes(i):
            result.append(i)
    return sorted(result)