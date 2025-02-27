def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    for _ in range(67):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal % fibonacci[68] == 0:
        return True
    else:
        return False