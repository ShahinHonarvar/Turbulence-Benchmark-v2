def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_54 = 2971215073
    return decimal % fibonacci_54 == 0