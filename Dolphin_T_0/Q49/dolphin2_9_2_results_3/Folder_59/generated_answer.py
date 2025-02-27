def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 74:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_str, 2)
    if decimal % fibonacci[73] == 0:
        return True
    else:
        return False