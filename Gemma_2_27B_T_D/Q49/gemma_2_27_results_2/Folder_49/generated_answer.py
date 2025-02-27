def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_95 = 2805711729925101407
    return decimal % fibonacci_95 == 0