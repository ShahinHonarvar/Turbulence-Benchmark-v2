def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = fibonacci(28)[28]
    return decimal % fib == 0