def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 176):
        fib.append(fib[-1] + fib[-2])
    fibonacci_176th = fib[175]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_176th == 0