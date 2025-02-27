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

def is_left_right_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:i])) or not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[30]
    result = []
    for num in range(x, 0, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)