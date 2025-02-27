def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while frozenset(fibonacci[-2:]) not in {frozenset([n, n + 1]) for n in fibonacci[-2:] if n + 1 <= decimal}:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal % fibonacci[-1] == 0:
        return True
    else:
        return False