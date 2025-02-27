def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        next = current + fibonacci(current)
        while next < 99:
            next = next + fibonacci(next)
        return next

    def get_decimal(binary_str):
        decimal = 0
        for i, bit in enumerate(binary_str):
            decimal += int(bit) * 2 ** i
        return decimal
    next_fibonacci = get_next_fibonacci(0)
    while get_decimal(binary_str) % next_fibonacci != 0:
        next_fibonacci = get_next_fibonacci(next_fibonacci)
    return True