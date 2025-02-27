def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 48):
        fib.append(fib[i - 2] + fib[i - 1])
    decimal_int = int(binary_str, base=2)
    for num in fib:
        if decimal_int % num == 0:
            return True
    return False