def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    a, b = (0, 1)
    fibonacci = [0, 1]
    for _ in range(84):
        a, b = (b, a + b)
        fibonacci.append(b)
    return decimal_number % fibonacci[84] == 0