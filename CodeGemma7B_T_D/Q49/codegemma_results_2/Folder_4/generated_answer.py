def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-2] + fib[-1])
    if num % fib[118] == 0:
        return True
    else:
        return False