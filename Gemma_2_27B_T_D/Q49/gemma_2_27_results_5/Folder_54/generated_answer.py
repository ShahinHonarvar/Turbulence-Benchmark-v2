def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_34 = 5702887
    return decimal_number % fibonacci_34 == 0