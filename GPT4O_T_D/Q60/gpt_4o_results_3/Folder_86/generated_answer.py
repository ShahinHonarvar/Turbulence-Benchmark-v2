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

def truncatable_left_right(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 127:
        return []
    x = numbers[126]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and truncatable_left_right(num):
            result.append(num)
    return sorted(result, reverse=True)