def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 100:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_integer % fibonacci[-1] == 0