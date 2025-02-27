def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[n - 1]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    n = 90
    fib = fibonacci(n)
    return decimal % fib == 0