def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for i in range(n):
            a, b = (b, a + b)
        return a
    fib_nums = [fibonacci(n) for n in range(40)]
    fib_nums_mod_160 = [fib_num % 160 for fib_num in fib_nums]
    idx = next((i for i, n in enumerate(fib_nums_mod_160) if n == int(binary_str, 2)), None)
    if idx is not None:
        return True
    else:
        return False