def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 188:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal_integer % fibonacci[187] == 0:
        return True
    else:
        return False