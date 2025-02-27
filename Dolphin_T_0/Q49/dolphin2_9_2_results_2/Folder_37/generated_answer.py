def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 46:
        fib.append(fib[-1] + fib[-2])
    num = int(binary, 2)
    if fib[45] != 0 and num % fib[45] == 0:
        return True
    return False