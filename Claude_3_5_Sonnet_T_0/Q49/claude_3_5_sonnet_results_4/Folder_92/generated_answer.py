def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 7:
        fib.append(fib[-1] + fib[-2])
    seventh_fib = fib[6]
    return decimal % seventh_fib == 0