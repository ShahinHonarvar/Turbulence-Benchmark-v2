def if_decimal_is_divisible(num):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal = 0
    for i, bit in enumerate(num):
        decimal += int(bit) * 2 ** i
    for i in range(10):
        if fibonacci(128 + i) % decimal == 0:
            return True
    return False