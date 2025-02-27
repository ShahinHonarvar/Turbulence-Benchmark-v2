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
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return len(str_n) == 0 or is_prime(int(str_n))

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)