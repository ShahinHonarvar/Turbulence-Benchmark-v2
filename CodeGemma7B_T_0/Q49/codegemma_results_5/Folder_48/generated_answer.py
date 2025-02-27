def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        if current == fibonacci(0):
            return fibonacci(1)
        for i in range(current + 1, fibonacci(len(str(current)) + 1)):
            if fibonacci(i) > current:
                return fibonacci(i)

    def get_decimal(binary_representation):
        decimal = 0
        for i, bit in enumerate(binary_representation):
            decimal += int(bit) * 2 ** i
        return decimal
    next_fibonacci = fibonacci(len(binary_representation))
    while True:
        if get_decimal(binary_representation) % next_fibonacci == 0:
            return True
        next_fibonacci = get_next_fibonacci(next_fibonacci)
        if next_fibonacci is None:
            return False