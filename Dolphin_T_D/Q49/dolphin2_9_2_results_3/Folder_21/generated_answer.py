def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    i = 0
    fib = [0, 1]
    while len(fib) < 195:
        fib.append(fib[-1] + fib[-2])
        i += 1
    target = fib[194]
    if num % target == 0:
        return True
    else:
        return False