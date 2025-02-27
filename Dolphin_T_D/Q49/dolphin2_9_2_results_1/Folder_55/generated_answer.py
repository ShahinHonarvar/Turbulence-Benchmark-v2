def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 39:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    decimal = int(binary_string, 2)
    return decimal % fibonacci[38] == 0