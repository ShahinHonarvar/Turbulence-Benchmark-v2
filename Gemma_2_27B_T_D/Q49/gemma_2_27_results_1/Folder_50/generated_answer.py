def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_119 = 1051793078142958948199619094940
    return decimal % fib_119 == 0