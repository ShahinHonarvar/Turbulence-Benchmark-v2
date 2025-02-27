def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_24 = 46368
    return decimal % fibonacci_24 == 0