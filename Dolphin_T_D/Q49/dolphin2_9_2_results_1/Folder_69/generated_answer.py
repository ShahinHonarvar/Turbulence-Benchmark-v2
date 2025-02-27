def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 170:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divider = fibonacci[169]
    return decimal % divider == 0