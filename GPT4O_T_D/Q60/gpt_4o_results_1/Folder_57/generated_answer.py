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
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        left_truncate = int(str_n[i:])
        right_truncate = int(str_n[:-i] or '0')
        if not (is_prime(left_truncate) and is_prime(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    result.sort(reverse=True)
    return result