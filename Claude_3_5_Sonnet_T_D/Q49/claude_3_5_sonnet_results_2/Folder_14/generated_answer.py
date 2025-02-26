def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 27:
        fib.append(fib[-1] + fib[-2])
    fibonacci_27th = fib[26]
    return decimal % fibonacci_27th == 0