def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = fibonacci(199)
    if decimal % fib == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)