def if_decimal_is_divisible(binary_rep):
    fibonacci = [0, 1]
    decimal = 0
    for bit in binary_rep:
        decimal = decimal * 2 + int(bit)
    for _ in range(2, 144):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    if decimal % fibonacci[143] == 0:
        return True
    else:
        return False