def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    sixth_fibonacci_number = 5
    return decimal_value % sixth_fibonacci_number == 0