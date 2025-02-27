def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal_value = int(binary_str, 2)
    fib_16 = fibonacci(16)
    return decimal_value % fib_16 == 0