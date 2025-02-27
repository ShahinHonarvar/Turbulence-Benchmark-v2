def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(2, 196):
        fib.append(fib[-1] + fib[-2])
    fibonacci_number_196 = fib[195]
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_number_196 == 0