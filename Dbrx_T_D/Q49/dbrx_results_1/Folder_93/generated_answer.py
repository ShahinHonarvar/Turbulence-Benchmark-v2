def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] < decimal_number:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal_number % fibonacci[59] == 0:
        return True
    else:
        return False