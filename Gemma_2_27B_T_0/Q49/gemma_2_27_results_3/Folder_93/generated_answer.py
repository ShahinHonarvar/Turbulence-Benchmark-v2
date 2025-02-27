def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_59 = 577831250
    return decimal_number % fibonacci_59 == 0