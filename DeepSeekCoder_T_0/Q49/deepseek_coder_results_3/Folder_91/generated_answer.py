def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1, 1, 2, 3, 5]
    return decimal_value % fibonacci[5] == 0