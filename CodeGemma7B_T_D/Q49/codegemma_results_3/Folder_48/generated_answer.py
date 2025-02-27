def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = 1
    for i in range(198):
        fib = fib + (fib - 1)
    if decimal % fib == 0:
        return True
    else:
        return False