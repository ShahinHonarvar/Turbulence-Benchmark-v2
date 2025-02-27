def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 40:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return num % fibonacci[40 - 1] == 0