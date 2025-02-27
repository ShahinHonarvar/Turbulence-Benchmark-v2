def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary_string):
        return int(binary_string, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_to_decimal = decimal_from_binary(binary_string)
    fib_index = 188
    fib_value = fibonacci(fib_index)
    return is_divisible(binary_to_decimal, fib_value)