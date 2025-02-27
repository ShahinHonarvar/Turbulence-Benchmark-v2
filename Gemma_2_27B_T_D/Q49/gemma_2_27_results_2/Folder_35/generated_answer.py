def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 187:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[186] == 0