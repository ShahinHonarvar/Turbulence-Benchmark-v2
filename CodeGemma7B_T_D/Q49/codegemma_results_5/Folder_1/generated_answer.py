def if_decimal_is_divisible(decimal_binary_representation):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_binary(n):
        if n == 0:
            return ''
        elif n % 2 == 0:
            return decimal_to_binary(n // 2) + '0'
        else:
            return decimal_to_binary(n // 2) + '1'

    def binary_to_decimal(n):
        return int(n, 2)

    def get_Fibonacci_90():
        i = 0
        while fibonacci(i) <= binary_to_decimal(decimal_binary_representation):
            i += 1
        return fibonacci(i)
    decimal = binary_to_decimal(decimal_binary_representation)
    if decimal % get_Fibonacci_90() == 0:
        return True
    else:
        return False