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

def is_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    length = len(num_str)
    for i in range(length):
        left_truncate = int(num_str[i:])
        right_truncate = int(num_str[:length - i])
        if not is_prime(left_truncate) or not is_prime(right_truncate):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 89:
        return []
    x = numbers[88]
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes