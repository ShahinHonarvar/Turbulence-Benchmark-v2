def if_decimal_is_divisible(binary_representation_str):

    def fibonacci(n):
        if n in [0, 1]:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_sequence = fibonacci(153)
    decimal_representation = int(binary_representation_str, 2)
    if decimal_representation % fibonacci_sequence == 0:
        return True
    else:
        return False