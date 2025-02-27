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

def is_left_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    result = [n for n in range(2, x) if is_prime(n) and is_left_truncatable_prime(n) and ('0' not in str(n))]
    return sorted(result, reverse=True)