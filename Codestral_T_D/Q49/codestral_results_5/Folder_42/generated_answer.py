def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 146:
        fib.append(fib[-1] + fib[-2])
    fib_146 = fib[146]
    return decimal % fib_146 == 0