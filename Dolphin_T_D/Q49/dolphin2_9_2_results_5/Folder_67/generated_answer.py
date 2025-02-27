def if_decimal_is_divisible(binary_representation):
    i = 0
    j = 1
    fib = 0
    while fib < 107:
        fib = i + j
        if fib > 107:
            break
        i, j = (j, fib)
    decimal = int(binary_representation, 2)
    return decimal % fib == 0