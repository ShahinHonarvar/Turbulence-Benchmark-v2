def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def get_decimal_from_binary(binary_str):
        return int(binary_str, 2)
    fibonacci_generator = get_next_fibonacci()
    for i in range(125):
        next(fibonacci_generator)
    if get_decimal_from_binary(binary_str) % next(fibonacci_generator) == 0:
        return True
    else:
        return False