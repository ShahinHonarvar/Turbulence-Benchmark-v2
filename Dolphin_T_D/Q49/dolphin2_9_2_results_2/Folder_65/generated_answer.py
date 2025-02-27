def if_decimal_is_divisible(bin_rep_of_decimal):
    decimal = int(bin_rep_of_decimal, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 127:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if decimal % fibonacci[-1] == 0:
        return True
    else:
        return False