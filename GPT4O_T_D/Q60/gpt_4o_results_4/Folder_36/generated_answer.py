def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable(num):
    s = str(num)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 993:
        return []
    x = numbers[992]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_left_right_truncatable(num):
            result.append(num)
    return result