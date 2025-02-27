def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    for i in range(2, 146):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal = 0
    for digit in binary_rep:
        decimal = decimal * 2 + int(digit)
    return decimal % fib[145] == 0