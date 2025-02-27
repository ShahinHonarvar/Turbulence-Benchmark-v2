def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    member = 0
    fib = [0, 1]
    while len(fib) < 66:
        fib.append(fib[-1] + fib[-2])
        member += 1
    if decimal_num % fib[65] == 0:
        return True
    return False