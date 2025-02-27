def if_decimal_is_divisible(binary_representation):
    binary_to_decimal = 0
    for i in range(len(binary_representation)):
        binary_to_decimal += int(binary_representation[len(binary_representation) - i - 1]) * 2 ** i
    return binary_to_decimal % fibonacci(195) == 0

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)