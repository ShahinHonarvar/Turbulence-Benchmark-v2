def if_decimal_is_divisible(binary):

    def fibonacci(num):
        return num <= 1 and num in [0, 1] or fibonacci(num - 1) + fibonacci(num - 2)
    decimal = int(binary, 2)
    fib_i = 1
    fib_num = fibonacci(fib_i)
    while decimal >= fib_num:
        if decimal == fib_num:
            return True
        fib_i += 1
        fib_num = fibonacci(fib_i)
    return False