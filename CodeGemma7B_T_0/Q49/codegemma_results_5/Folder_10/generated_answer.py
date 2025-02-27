def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 1:
            return None
        return fibonacci(n - 1)

    def get_decimal_value(binary_representation):
        return int(binary_representation, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    nth_fibonacci = get_nth_fibonacci(88)
    decimal_value = get_decimal_value(binary_representation)
    return is_divisible(decimal_value, nth_fibonacci)