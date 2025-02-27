def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    target_fibonacci_number = fibonacci_numbers[4]
    if decimal_number % target_fibonacci_number == 0:
        return True
    else:
        return False