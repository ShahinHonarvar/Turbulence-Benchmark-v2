def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_67 = fibonacci(67)
    if decimal_integer % fib_67 == 0:
        return True
    else:
        return False