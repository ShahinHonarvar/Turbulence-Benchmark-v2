def if_decimal_is_divisible(bin_num):
    decimal = int(bin_num, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 54:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[53] == 0