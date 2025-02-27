def if_decimal_is_divisible(bin_repr):
    decimal_num = int(bin_repr, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 80:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_num % fibonacci[79] == 0