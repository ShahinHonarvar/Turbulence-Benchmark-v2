def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fourth_fibonacci_number = 3
    return decimal_number % fourth_fibonacci_number == 0