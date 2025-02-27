def if_decimal_is_divisible(n):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    fib = 109
    while fib < int(n, 2):
        fib += 1
        fibonacci(fib)
    return fibonacci(109) != 0 and int(n, 2) % fibonacci(109) == 0