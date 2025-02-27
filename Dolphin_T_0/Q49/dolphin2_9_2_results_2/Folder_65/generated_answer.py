def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 126:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return decimal % fibonacci[-1] == 0