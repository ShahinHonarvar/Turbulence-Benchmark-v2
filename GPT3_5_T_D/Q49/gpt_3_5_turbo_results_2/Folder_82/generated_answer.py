def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 100:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary, 2)
    return decimal % fibonacci[98] == 0