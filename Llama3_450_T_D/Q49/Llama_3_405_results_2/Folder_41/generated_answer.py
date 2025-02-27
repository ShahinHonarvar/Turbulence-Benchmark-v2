def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal_num = int(binary_str, 2)
    fibonacci_67 = fibonacci(67)
    return decimal_num % fibonacci_67 == 0