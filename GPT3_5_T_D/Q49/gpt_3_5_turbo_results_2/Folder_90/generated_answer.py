def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    n = 2
    while len(fibonacci) <= 177:
        fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])
        n += 1
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci[177] == 0