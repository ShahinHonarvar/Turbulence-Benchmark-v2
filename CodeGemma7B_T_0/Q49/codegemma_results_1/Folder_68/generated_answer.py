def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        while True:
            current += 1
            if fibonacci(current) > 38:
                return fibonacci(current)

    def get_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal
    if get_next_fibonacci(get_decimal(binary_representation)) % get_decimal(binary_representation) == 0:
        return True
    return False