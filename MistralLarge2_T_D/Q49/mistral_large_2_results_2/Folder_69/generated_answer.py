def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[n]

def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_170 = fibonacci(170)
    return decimal_value % fib_170 == 0