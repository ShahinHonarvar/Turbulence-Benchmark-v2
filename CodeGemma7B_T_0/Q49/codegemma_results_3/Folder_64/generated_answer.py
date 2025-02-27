def if_decimal_is_divisible(binary_representation):

    def get_next_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fibonacci_generator = get_next_fibonacci()
    for _ in range(10):
        next(fibonacci_generator)
    if get_decimal_value(binary_representation) % next(fibonacci_generator) == 0:
        return True
    else:
        return False