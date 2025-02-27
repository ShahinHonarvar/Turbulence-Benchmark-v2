def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_120 = 0
    fib_119 = 1
    for _ in range(2, 121):
        fib_120, fib_119 = (fib_119, fib_120 + fib_119)
    return decimal % fib_120 == 0