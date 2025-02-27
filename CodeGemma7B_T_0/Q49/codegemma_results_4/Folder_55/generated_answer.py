def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 39):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal = int(binary_str, 2)
    if decimal % fib[38] == 0:
        return True
    else:
        return False