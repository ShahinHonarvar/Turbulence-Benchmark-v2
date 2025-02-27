def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    return decimal_representation % fibonacci(115) == 0

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)