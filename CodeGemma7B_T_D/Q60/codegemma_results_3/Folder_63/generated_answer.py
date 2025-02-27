def all_left_right_truncatable_prime(numbers):
    list = []
    for i in range(len(numbers)):
        if is_prime(numbers[i]) and has_no_zero(numbers[i]) and is_truncatable_prime(numbers[i]):
            list.append(numbers[i])
    list.sort()
    return list

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def has_no_zero(x):
    if '0' in str(x):
        return False
    return True

def is_truncatable_prime(x):
    if x < 10:
        return False
    for i in range(int(str(x)[len(str(x)) - 1])):
        x = int(str(x)[:-1])
        if not is_prime(x):
            return False
    for i in range(len(str(x)) - 1):
        x = int(str(x)[1:])
        if not is_prime(x):
            return False
    return True