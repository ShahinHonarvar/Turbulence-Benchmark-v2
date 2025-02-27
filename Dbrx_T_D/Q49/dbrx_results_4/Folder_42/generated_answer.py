def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    for _ in range(144):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_integer % fibonacci[145] == 0