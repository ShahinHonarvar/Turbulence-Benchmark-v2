def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    i = 0
    while fibonacci[i] <= decimal:
        fibonacci.append(fibonacci[0] + fibonacci[1])
        fibonacci[0] = fibonacci[1]
        fibonacci[1] = fibonacci[2]
        i += 1
    return fibonacci[46] % decimal == 0