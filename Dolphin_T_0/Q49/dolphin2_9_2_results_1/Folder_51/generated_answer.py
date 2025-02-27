def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 17:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[16] != 0 and decimal % fibonacci[16] == 0