def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
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
    str_n = str(n)
    while len(str_n) > 1:
        if '0' in str_n:
            return False
        if not is_prime(int(str_n)) or not is_prime(int(str_n[::-1])):
            return False
        str_n = str_n[1:-1]
    return is_prime(int(str_n)) and len(str_n) == 1 and is_prime(int(str_n[::-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)