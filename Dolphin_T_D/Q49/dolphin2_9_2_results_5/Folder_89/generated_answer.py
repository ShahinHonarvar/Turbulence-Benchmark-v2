def if_decimal_is_divisible(binary_string):
    if not all((c in '01' for c in binary_string)):
        return False
    num_decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 126:
        fib.append(fib[-1] + fib[-2])
    return num_decimal % fib[125] == 0