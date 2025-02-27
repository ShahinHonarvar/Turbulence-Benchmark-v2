def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fib47 = fibonacci(47)
    decimal = int(binary, 2)
    return decimal % fib47 == 0