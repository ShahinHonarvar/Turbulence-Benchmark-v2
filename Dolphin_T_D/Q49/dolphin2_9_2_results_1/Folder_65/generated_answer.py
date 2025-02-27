def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_127 = fibonacci(127)
    if decimal % fib_127 == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)