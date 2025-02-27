def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(n):
    decimal_num = int(n, 2)
    fib_num = fibonacci(110)
    return decimal_num % fib_num == 0