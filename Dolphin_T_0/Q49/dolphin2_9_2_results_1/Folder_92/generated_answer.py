def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] < decimal:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] == 7:
        return True
    else:
        return False