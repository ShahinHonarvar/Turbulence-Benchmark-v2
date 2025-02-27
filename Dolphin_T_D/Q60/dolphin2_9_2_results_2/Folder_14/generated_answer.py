def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def left_right_truncatable(number):
    if len(str(number)) <= 2:
        return is_prime(number)
    for i in range(6):
        number = number // 10 if i % 2 == 0 else number % 10 ** str(number)[-i - 1:-i] * 10 ** (len(str(number)) - i - 2) + number % 10 ** (len(str(number)) - i - 1)
        if number < 10 and (not is_prime(number)):
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    result = []
    max_val = int(tuple_of_positive_integers[78])
    for i in range(max_val, 1, -1):
        if is_prime(i) and left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)