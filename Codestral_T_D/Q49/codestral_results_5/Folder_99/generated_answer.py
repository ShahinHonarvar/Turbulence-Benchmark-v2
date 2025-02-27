def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 109:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
    if decimal % fib[109 - 1] == 0:
        return True
    else:
        return False