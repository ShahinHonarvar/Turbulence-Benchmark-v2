def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 17:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_value % fibonacci[15] == 0