def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1, 1, 2, 3, 5]
    return decimal % fib[5] == 0