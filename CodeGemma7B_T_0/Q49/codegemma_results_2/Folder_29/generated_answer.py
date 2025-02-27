def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 1:
            raise ValueError('Index out of range')
        return fibonacci(n - 1)

    def get_decimal_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    nth_fibonacci = get_nth_fibonacci(117)
    decimal_value = get_decimal_value(binary_str)
    return is_divisible(decimal_value, nth_fibonacci)