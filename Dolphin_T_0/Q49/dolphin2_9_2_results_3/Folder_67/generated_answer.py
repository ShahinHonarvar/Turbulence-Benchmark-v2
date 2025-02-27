def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    n = 0
    while fibonacci(n) < 2 ** 30:
        n += 1
    number = int(binary, 2)
    return number % fibonacci(n) == 0