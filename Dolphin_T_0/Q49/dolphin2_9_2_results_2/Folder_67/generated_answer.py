def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    while fibonacci[-2] + fibonacci[-1] < decimal:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci[-1] * fibonacci[-2] == decimal or fibonacci[-2] * fibonacci[-1] == decimal or fibonacci[-1] * fibonacci[-2] == decimal or (fibonacci[-2] * fibonacci[-1] == decimal)