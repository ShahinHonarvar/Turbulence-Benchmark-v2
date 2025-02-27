def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fib_100 = fibonacci(100)
    return decimal_number % fib_100 == 0