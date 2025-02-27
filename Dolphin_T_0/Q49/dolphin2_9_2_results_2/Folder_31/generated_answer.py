def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fib_69 = fibonacci(69)
    decimal = int(binary_str, 2)
    return decimal % fib_69 == 0