def if_decimal_is_divisible(binary_repr):
    decimal = int(binary_repr, 2)
    fibonacci = [0, 1]
    for _ in range(2, 19):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[-1] == 0