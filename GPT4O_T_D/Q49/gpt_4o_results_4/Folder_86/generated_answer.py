def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    for i in range(2, 135):
        fib.append(fib[-1] + fib[-2])
    fib135 = fib[134]
    decimal_integer = int(binary_rep, 2)
    return decimal_integer % fib135 == 0