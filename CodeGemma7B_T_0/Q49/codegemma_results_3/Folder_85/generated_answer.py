def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_gen = get_next_fibonacci()
    fib_list = [next(fib_gen) for _ in range(45)]
    return int(binary_str, 2) % fib_list[-1] == 0