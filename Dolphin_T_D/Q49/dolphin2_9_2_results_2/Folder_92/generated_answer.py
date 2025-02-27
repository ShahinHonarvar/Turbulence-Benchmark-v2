def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
    return decimal % fibonacci[6] == 0