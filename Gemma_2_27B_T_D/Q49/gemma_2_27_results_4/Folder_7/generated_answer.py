def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_160 = 7.868493242095774e+33
    return decimal % fib_160 == 0