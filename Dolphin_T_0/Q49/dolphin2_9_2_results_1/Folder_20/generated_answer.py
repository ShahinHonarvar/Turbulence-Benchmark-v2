def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci = [0, 1]
    i = 2
    while fibonacci[i - 1] + fibonacci[i - 2] <= decimal:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1
    if fibonacci[-1] == 0:
        return True
    return decimal % fibonacci[-2] == 0