def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_from_binary(binary):
        return int(binary, 2)
    decimal = decimal_from_binary(binary)
    i = 1
    while decimal_from_binary(fibonacci(i)) < decimal:
        i += 1
    return decimal % fibonacci(i) == 0