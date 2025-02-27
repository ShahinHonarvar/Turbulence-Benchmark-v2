def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 34:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n % fibonacci[33] == 0