def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary):
        return int(binary, 2)
    binary_number = decimal_from_binary(binary_representation)
    fibonacci_160th = fibonacci(160)
    return binary_number % fibonacci_160th == 0