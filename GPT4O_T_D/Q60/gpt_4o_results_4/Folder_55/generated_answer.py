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

def is_truncatable_prime(num):
    s = str(num)
    if '0' in s:
        return False
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)