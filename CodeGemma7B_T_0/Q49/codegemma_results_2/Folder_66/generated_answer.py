def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary_representation):
        return int(binary_representation, 2)

    def is_divisible(number, divisor):
        return number % divisor == 0
    binary_length = len(binary_representation)
    decimal = decimal_from_binary(binary_representation)
    for i in range(binary_length):
        if is_divisible(decimal, fibonacci(i + 1)):
            return True
    return False