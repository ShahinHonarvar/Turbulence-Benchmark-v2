def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary_representation):
        return int(binary_representation, 2)

    def is_divisible(number, divisor):
        return number % divisor == 0
    return is_divisible(decimal_from_binary(binary_representation), fibonacci(47))