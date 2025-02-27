def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_56 = 1
    a = 0
    b = 1
    for i in range(2, 56):
        fib_56 = a + b
        a = b
        b = fib_56
    return decimal_value % fib_56 == 0