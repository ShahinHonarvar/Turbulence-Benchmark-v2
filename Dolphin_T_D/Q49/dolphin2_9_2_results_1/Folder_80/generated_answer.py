def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    a, b = (0, 1)
    for i in range(179):
        a, b = (b, a + b)
    fibonacci_179th = a
    return decimal_number % fibonacci_179th == 0