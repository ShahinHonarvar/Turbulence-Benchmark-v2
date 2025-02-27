def if_decimal_is_divisible(binary_decimal):
    decimal = int(binary_decimal, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 159:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[158] != 0 and decimal % fibonacci[158] == 0:
        return True
    return False