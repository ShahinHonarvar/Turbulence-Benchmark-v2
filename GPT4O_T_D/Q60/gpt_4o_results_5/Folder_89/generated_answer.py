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

def is_no_zero(n):
    return '0' not in str(n)

def is_left_right_truncatable_prime(n):
    s = str(n)
    length = len(s)
    for i in range(1, length):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[97]
    result = []
    for num in range(11, x + 1):
        if is_no_zero(num) and is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)