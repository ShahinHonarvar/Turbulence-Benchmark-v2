def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_87 = 354224848179261915075
    return decimal_num % fib_87 == 0