def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_45 = fibonacci(45)
    return decimal_integer % fib_45 == 0

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)