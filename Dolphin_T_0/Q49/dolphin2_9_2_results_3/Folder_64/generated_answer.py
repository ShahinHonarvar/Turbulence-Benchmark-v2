def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 10:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal_num % fibonacci[-1] == 0:
        return True
    else:
        return False