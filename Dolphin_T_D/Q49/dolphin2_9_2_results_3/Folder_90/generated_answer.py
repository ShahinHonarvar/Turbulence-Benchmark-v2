def if_decimal_is_divisible(bin_str):
    fib_177 = [0, 1]
    while len(fib_177) < 177:
        fib_177.append(fib_177[-1] + fib_177[-2])
    decimal = int(bin_str, 2)
    return decimal % fib_177[176] == 0