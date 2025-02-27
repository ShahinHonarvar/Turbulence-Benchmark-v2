def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0]
    a, b = (0, 1)
    while len(fibonacci) < 185:
        a, b = (b, a + b)
        fibonacci.append(a)
    return decimal % fibonacci[184] == 0