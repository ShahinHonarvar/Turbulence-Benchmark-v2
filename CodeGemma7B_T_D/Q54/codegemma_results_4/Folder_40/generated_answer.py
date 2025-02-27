def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if not is_prime(int(str_num[:i])):
            return False
    return True

def all_right_truncatable_prime(tuple):
    x = tuple[10]
    result = []
    for num in range(x):
        if is_prime(num):
            if right_truncatable(num):
                result.append(num)
    result.sort(reverse=True)
    return result