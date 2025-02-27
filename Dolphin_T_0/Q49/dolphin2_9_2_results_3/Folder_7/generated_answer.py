def if_decimal_is_divisible(binary_string):
    binary_to_decimal = lambda binary_string: int(binary_string, 2)
    fibonacci = [0, 1]
    for _ in range(2, 160):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = binary_to_decimal(binary_string)
    return decimal % fibonacci[160] == 0