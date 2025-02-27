def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 166:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    if decimal % fibonacci[165] == 0:
        return True
    else:
        return False