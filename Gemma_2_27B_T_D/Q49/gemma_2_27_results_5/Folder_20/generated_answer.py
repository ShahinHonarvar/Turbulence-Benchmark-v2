def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_100th = 354224848179261915075
    return decimal_value % fibonacci_100th == 0