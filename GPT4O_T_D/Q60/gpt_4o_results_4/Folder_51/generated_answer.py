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

def is_left_right_truncatable_prime(n):
    s = str(n)
    length = len(s)
    for i in range(length):
        left_truncate = int(s[i:])
        right_truncate = int(s[:length - i])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 55:
        return []
    x = numbers[54]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes