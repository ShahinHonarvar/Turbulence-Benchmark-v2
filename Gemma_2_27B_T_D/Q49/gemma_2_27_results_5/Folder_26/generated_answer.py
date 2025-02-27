def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    return decimal_value % fibonacci(138) == 0