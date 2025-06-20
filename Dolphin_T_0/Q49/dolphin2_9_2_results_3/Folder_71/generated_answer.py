def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib147 = fibonacci(147)
    return decimal % fib147 == 0