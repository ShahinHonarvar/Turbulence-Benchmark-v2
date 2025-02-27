def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 109:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal % fibonacci[108] == 0:
        return True
    else:
        return False