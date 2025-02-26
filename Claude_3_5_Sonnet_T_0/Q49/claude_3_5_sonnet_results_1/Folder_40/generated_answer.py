def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1, 1, 2]
    return decimal % fib[3] == 0