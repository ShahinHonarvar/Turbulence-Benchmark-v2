def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fib_num = 0
    a, b = (0, 1)
    for _ in range(164):
        fib_num = a
        a, b = (b, a + b)
    return decimal_num % fib_num == 0