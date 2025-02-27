def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= 186:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    return decimal % fibonacci[186] == 0