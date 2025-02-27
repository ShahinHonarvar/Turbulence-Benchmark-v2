def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    for _ in range(115):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal % fibonacci[116] == 0:
        return True
    else:
        return False