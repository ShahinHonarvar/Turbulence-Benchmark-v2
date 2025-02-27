def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_truncatable_prime(number):
    result = []
    for digit in list(str(number[43]))[:-1:-1]:
        if digit == '0':
            continue
        current_number = int(digit)
        if is_prime(current_number):
            result.append(current_number)
    return sorted(result)