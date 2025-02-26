def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 11:
        fib.append(fib[-1] + fib[-2])
    tenth_fib = fib[10]
    return decimal % tenth_fib == 0