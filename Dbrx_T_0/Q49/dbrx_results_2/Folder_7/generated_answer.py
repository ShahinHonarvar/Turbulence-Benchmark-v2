def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = 0
    previous_number = -1
    current_number = 0
    for _ in range(160):
        fibonacci_number = current_number + previous_number
        previous_number = current_number
        current_number = fibonacci_number
    return decimal_integer % fibonacci_number == 0