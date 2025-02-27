def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 166:
        fib.append(fib[-1] + fib[-2])
    fib_166 = fib[165]
    return decimal % fib_166 == 0