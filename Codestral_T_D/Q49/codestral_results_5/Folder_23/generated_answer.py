def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_str, 2)
    fib_48 = fibonacci(48)
    if decimal_num % fib_48 == 0:
        return True
    else:
        return False