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

def truncate_number(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 100:
        return []
    x = numbers[100]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num) and truncate_number(num):
            result.append(num)
    return result