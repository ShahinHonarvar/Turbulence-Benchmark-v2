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
    if '0' in str(prime):
        return False
    str_prime = str(prime)
    for i in range(len(str_prime)):
        if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:len(str_prime) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 992:
        return []
    x = numbers[992]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    return sorted(result)