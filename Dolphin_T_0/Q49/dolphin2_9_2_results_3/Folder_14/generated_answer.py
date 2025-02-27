def if_decimal_is_divisible(binary):
    decimal_val = int(binary, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 27:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_val % fibonacci[-1] == 0