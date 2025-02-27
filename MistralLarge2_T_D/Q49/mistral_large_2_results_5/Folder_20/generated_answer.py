def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fib_100 = 354224848179261915075
    return decimal_integer % fib_100 == 0