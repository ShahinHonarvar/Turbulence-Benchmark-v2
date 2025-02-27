def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 34):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if decimal_integer % fibonacci[33] == 0:
        return True
    else:
        return False