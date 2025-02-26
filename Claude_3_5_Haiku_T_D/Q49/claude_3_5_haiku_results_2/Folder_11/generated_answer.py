def if_decimal_is_divisible(binary_string):

    def fibonacci_16th():
        fib_sequence = [0, 1]
        while len(fib_sequence) < 16:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[15]
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_16th() == 0