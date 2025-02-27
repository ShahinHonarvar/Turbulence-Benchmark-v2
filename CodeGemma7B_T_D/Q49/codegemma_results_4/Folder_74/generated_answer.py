def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_166 = fibonacci(166)
    return decimal_integer % fib_166 == 0