def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    fib_list = [fibonacci(i) for i in range(35)]
    return int(binary, 2) % fib_list[34] == 0