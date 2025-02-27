def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= decimal:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-2] * fibonacci[-1] == 0 or decimal % fibonacci[-2] == 0