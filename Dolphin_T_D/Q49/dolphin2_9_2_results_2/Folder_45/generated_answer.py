def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_28 = fibonacci(28)
    return decimal_number % fib_28 == 0

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)