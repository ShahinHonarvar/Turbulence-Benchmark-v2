def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 150:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_number % fibonacci[149] == 0