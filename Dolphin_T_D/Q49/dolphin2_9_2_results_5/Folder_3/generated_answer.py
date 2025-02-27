def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_35 = [0, 1]
    while len(fibonacci_35) < 35:
        fibonacci_35.append(fibonacci_35[-1] + fibonacci_35[-2])
    if decimal % fibonacci_35[34] == 0:
        return True
    else:
        return False