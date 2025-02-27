def if_decimal_is_divisible(binary_representation):

    def get_next_fibonacci():
        first = 0
        second = 1
        while True:
            next = first + second
            first = second
            second = next
            yield next

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value
    fibonacci_generator = get_next_fibonacci()
    for _ in range(134):
        next_fibonacci = next(fibonacci_generator)
    if get_decimal_value(binary_representation) % next_fibonacci == 0:
        return True
    return False