def if_decimal_is_divisible(binary_str):

    def fibonacci_6th():
        fib_sequence = [0, 1, 1, 2, 3, 5]
        return fib_sequence[5]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_6th() == 0