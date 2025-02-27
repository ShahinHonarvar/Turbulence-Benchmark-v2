def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while len(fibonacci) <= 104:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_value = int(binary_representation, 2)
    return decimal_value % fibonacci[104] == 0