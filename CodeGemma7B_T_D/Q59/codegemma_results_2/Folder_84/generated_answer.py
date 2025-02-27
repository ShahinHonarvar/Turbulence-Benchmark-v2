def all_left_truncatable_prime(n):
    result = []
    for number in range(n):
        if is_prime(number) and has_no_zero(number) and all_left_truncatable(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def has_no_zero(number):
    return '0' not in str(number)

def all_left_truncatable(number):
    str_number = str(number)
    for i in range(1, len(str_number)):
        if not is_prime(int(str_number[i:])):
            return False
    return True