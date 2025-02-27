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

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    str_num = str(num)
    while len(str_num) > 1:
        str_num = str_num[:-1]
        if not is_prime(int(str_num)):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[11]
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)