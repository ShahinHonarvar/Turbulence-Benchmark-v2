def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_39 = 63245986
    return decimal % fibonacci_39 == 0