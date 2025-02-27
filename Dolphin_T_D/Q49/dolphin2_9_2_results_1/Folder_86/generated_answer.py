def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_135 = fibonacci(135)
    if decimal % fib_135 == 0:
        return True
    else:
        return False