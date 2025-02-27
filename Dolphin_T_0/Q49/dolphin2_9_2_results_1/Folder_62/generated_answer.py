def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 130:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return dec % fibonacci[-1] == 0