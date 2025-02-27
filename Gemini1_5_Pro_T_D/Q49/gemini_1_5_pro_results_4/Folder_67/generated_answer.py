def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    for _ in range(107):
        a, b = (b, a + b)
    fibonacci_number = a
    return decimal_representation % fibonacci_number == 0