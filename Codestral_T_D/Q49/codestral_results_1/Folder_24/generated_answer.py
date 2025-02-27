def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 56:
        fib.append(fib[-1] + fib[-2])
    fibonacci_56 = fib[55]
    return decimal % fibonacci_56 == 0