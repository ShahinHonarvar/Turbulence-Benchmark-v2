def if_decimal_is_divisible(binary_representation):
    binary_representation = binary_representation[:27]
    decimal_representation = int(binary_representation, 2)
    fib_number = fibonacci(119)
    return decimal_representation % fib_number == 0

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)