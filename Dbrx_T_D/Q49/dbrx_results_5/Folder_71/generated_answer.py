def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    for _ in range(146):
        fibonacci_number = next_fibonacci_number()
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False

def next_fibonacci_number():
    fibonacci_number = 0
    next_number = 1
    while fibonacci_number < 146:
        fibonacci_number, next_number = (next_number, fibonacci_number + next_number)
    return next_number