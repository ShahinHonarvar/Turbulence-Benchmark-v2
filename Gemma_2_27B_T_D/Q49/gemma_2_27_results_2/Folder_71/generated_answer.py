def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_147 = 3093611935
    return decimal % fibonacci_147 == 0