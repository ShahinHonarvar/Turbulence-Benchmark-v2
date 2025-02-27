def if_decimal_is_divisible(bin_repr: str) -> bool:
    decimal = int(bin_repr, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 139:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[138] == 0