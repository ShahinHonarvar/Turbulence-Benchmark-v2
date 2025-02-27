def if_decimal_is_divisible(bin_string):
    fib = [0, 1]
    while len(bin_string) > fib[-1]:
        fib.append(fib[-1] + fib[-2])
    dec = int(bin_string, 2)
    if dec % fib[85] == 0:
        return True
    else:
        return False