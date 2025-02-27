def if_decimal_is_divisible(binary_string):

    def get_fibonacci():
        first, second = (0, 1)
        sequence = [first]
        while True:
            first, second, sequence = (second, first + second, sequence + [second])
            yield sequence[-1]
    fib_generator = get_fibonacci()
    fib_number = next(fib_generator)
    decimal = int(binary_string, 2)
    while decimal % fib_number != 0:
        fib_number = next(fib_generator)
    return True