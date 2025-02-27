def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_97 = fibonacci(97)
    return decimal % fib_97 == 0