def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(67):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci[69] == 0