def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1, 1, 2, 3, 5, 8]
    fourth_fibonacci = fibonacci[4]
    return decimal_value % fourth_fibonacci == 0