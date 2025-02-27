def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 84:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divider = fibonacci[-1]
    if decimal % divider == 0:
        return True
    else:
        return False