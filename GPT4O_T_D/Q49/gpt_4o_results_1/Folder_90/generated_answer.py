def if_decimal_is_divisible(binary_str):
    fib_cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n in fib_cache:
            return fib_cache[n]
        fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_cache[n]
    nth_fib_number = fibonacci(177)
    decimal_value = int(binary_str, 2)
    return decimal_value % nth_fib_number == 0