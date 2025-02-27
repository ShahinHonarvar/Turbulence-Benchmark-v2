def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_95 = [0, 1]
    for i in range(2, 96):
        fib_95.append(fib_95[i - 1] + fib_95[i - 2])
    fib_95 = fib_95[-1]
    if decimal % fib_95 == 0:
        return True
    else:
        return False