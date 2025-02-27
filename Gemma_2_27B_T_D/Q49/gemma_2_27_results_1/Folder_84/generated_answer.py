def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci = [0, 1]
    for _ in range(2, 196):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_value % fibonacci[-1] == 0