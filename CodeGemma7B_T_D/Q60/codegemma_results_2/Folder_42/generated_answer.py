def all_left_right_truncatable_prime(x):
    result = []
    for number in range(2, x + 1):
        if is_prime(number):
            if is_truncatable(number):
                result.append(number)
    result.sort(reverse=True)
    return result

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_truncatable(number):
    str_number = str(number)
    if '0' in str_number:
        return False
    for i in range(1, len(str_number)):
        if not is_prime(int(str_number[i:])):
            return False
    return True