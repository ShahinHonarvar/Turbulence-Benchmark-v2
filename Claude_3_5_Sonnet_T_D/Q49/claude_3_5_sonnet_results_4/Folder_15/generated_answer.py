def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 9:
        fib.append(fib[-1] + fib[-2])
    ninth_fibonacci = fib[8]
    return decimal % ninth_fibonacci == 0