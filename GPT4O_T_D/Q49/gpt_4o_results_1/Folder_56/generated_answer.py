def if_decimal_is_divisible(binary_string):
    fib_cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n not in fib_cache:
            fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_cache[n]
    fib_84 = fibonacci(84)
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_84 == 0