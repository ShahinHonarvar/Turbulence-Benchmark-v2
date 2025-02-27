def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1, 1, 2, 3, 5, 8]
    return decimal % fibonacci[5] == 0