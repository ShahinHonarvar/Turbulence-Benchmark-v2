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

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    temp = n
    factor = 1
    length = len(str(n))
    for _ in range(length):
        if not is_prime(temp):
            return False
        temp %= 10 ** (length - factor)
        factor += 1
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) <= 784:
        return []
    x = numbers[784]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)