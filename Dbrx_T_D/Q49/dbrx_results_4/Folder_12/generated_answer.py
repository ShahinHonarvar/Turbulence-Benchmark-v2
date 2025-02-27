def is_decimal_divisible(binary_string):
    fibonacci = [0, 1]
    while fibonacci[-1] < 66:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_string, 2)
    if decimal_number % fibonacci[-1] == 0:
        return True
    else:
        return False