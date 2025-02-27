def if_decimal_is_divisible(binary_string):
    fibonacci_24th = 28657
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_24th == 0