def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_94 = fibonacci(94)
    return decimal_number % fib_94 == 0