def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_179 = fibonacci(179)
    return decimal % fib_179 == 0