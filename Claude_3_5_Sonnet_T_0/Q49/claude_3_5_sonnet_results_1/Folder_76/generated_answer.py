def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    for _ in range(186):
        fib.append(fib[-1] + fib[-2])
    fibonacci_188 = fib[-1]
    return decimal % fibonacci_188 == 0