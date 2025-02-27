def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    a, b = (0, 1)
    for _ in range(108):
        a, b = (b, a + b)
    fibo_109 = b
    return decimal_number % fibo_109 == 0