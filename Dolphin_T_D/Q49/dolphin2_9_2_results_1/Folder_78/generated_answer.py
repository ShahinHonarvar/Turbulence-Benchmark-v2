def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fib = [[0, 1]]
    while len(fib[-1]) < num:
        fib.append([fib[-2][0] + fib[-2][1], fib[-1][0]])
    if num % fib[-1][0] == 0:
        return True
    return False