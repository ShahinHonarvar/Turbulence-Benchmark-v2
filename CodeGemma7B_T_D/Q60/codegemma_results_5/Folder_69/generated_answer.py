def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_left_truncatable_prime(number):
    str_number = str(number)
    for i in range(1, len(str_number)):
        if not is_prime(int(str_number[i:])):
            return False
    return True

def is_right_truncatable_prime(number):
    str_number = str(number)
    for i in range(2, len(str_number)):
        if not is_prime(int(str_number[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for number in range(2, x + 1):
        if is_prime(number) and is_left_truncatable_prime(number) and is_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)