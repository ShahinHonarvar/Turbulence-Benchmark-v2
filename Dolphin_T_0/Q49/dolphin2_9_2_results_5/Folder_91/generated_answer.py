def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 6:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divisor = fibonacci[5]
    return decimal % divisor == 0