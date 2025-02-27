def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_175 = 354224848179261915075
    return decimal_value % fib_175 == 0