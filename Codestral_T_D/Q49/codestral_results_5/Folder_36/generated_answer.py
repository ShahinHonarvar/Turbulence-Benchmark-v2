def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    a, b = (0, 1)
    for _ in range(150):
        a, b = (b, a + b)
    fib_150 = a
    return decimal_number % fib_150 == 0