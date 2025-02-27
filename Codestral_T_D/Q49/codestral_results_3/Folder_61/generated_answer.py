def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 76:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci_76 = fibonacci[75]
    return decimal % fibonacci_76 == 0