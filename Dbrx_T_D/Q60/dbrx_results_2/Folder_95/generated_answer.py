from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[77]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

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

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    string_num = str(num)
    if '0' in string_num:
        return False
    for i in range(1, len(string_num)):
        if not is_prime(int(string_num[i:])) or not is_prime(int(string_num[:-i])):
            return False
    return True