def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_179 = 354224848179261915075
    return decimal % fibonacci_179 == 0