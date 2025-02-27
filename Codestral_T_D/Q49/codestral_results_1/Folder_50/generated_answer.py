def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib = [0, 1]
    while len(fib) < 119:
        fib.append(fib[-1] + fib[-2])
    fibonacci_num = fib[118]
    return decimal % fibonacci_num == 0