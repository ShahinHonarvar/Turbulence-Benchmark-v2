def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fib_index = 78
    a, b = (0, 1)
    for _ in range(fib_index):
        a, b = (b, a + b)
    return n % b == 0