def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= 9:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if n % fibonacci[9] == 0:
        return True
    else:
        return False