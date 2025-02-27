def if_decimal_is_divisible(bin_repr):
    decimal = int(bin_repr, 2)
    fibonacci = [0, 1]
    while True:
        next_fibonacci = fibonacci[-1] + fibonacci[-2]
        if next_fibonacci > 85:
            break
        fibonacci.append(next_fibonacci)
    return decimal % fibonacci[84] == 0