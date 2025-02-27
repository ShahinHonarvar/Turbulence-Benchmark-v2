def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 45:
        fib.append(fib[-1] + fib[-2])
    fibonacci_45 = fib[45]
    return decimal % fibonacci_45 == 0