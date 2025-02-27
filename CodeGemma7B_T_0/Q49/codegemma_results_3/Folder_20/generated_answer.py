def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal(binary):
        return int(binary, 2)
    for i in range(len(binary)):
        if fibonacci(i + 1) == decimal(binary[:i + 1]) and fibonacci(i + 2) == decimal(binary[:i + 2]):
            return True
    return False