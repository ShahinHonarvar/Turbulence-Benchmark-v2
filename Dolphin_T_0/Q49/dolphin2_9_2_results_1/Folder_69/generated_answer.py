def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_170 = fibonacci(170)
    if decimal % fib_170 == 0:
        return True
    else:
        return False