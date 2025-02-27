def if_decimal_is_divisible(binary_str):
    fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
    for i in range(48):
        if fib(i) <= int(binary_str, 2):
            return i % 48 == 0
    return False