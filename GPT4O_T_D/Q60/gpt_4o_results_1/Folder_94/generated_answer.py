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
    for _ in range(len(s) - 1):
        if not is_prime(int(s)) or not is_prime(int(s[::-1])):
            return False
        s = s[1:]
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 43:
        return []
    x = numbers[43]
    result = []
    for num in range(11, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)