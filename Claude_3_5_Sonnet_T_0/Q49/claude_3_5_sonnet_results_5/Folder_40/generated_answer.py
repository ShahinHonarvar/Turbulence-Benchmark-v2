def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1, 1, 2]
    for _ in range(4):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[3] == 0