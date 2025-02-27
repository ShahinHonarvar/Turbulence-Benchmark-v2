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
    str_n = str(n)
    length = len(str_n)
    for i in range(length):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(tpl):
    x = tpl[97]
    result = []
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            result.append(n)
    return sorted(result)