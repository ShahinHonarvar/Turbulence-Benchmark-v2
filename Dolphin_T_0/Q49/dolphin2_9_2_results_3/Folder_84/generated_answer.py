def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 196:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return decimal % fibonacci[195] == 0