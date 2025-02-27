def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    for _ in range(184):
        fib.append(fib[-1] + fib[-2])
    fibonacci_185 = fib[185]
    decimal_integer = int(binary_rep, 2)
    return decimal_integer % fibonacci_185 == 0