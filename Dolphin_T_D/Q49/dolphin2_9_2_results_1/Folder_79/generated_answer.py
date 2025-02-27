def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_13th = fibonacci(13)
    if int(binary_string, 2) % fibonacci_13th == 0:
        return True
    return False