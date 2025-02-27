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

def left_truncatable(n):
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_prime(numbers):
    n = numbers[86]
    result = []
    for i in range(2, n):
        if '0' not in str(i) and left_truncatable(i):
            result.append(i)
    return result