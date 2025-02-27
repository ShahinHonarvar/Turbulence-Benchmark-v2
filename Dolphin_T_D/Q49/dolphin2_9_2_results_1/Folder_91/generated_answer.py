def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    return decimal % fibonacci[5] == 0