def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(num):
    str_num = str(num)
    while len(str_num) > 0:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[:-1]
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[96]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)