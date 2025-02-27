def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, len(binary_str)):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal = int(binary_str, 2)
    for i in range(len(fib)):
        if fib[i] == decimal and decimal % fib[i + 1] == 0:
            return True
    return False