def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    i = 2
    while i < 189:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        i += 1
    if decimal % fibonacci[188] == 0:
        return True
    else:
        return False