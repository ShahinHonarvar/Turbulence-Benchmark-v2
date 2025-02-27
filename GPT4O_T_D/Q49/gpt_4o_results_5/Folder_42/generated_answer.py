def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(2, 147):
        fib.append(fib[-1] + fib[-2])
    fib_146th = fib[146]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_146th == 0