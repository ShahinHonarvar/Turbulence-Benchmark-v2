def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    i = 2
    result = 0
    while len(fib) <= 134:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    for char in binary_str:
        result = (result << 1) + int(char)
    return result % fib[134] == 0