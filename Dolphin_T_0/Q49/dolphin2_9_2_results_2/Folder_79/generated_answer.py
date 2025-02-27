def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while fibonacci[-1] < 2 ** len(binary):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return int(binary, 2) % fibonacci[13] == 0