def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 7:
        fib.append(fib[-1] + fib[-2])
    fib_number = fib[6]
    if decimal % fib_number == 0:
        return True
    else:
        return False