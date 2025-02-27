def if_decimal_is_divisible(binary_str):
    dec = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) <= 174:
        fib.append(fib[-1] + fib[-2])
    if dec % fib[-1] == 0:
        return True
    else:
        return False