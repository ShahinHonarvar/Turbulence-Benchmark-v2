def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    n = 176
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[n - 1] == 0