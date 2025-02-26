def if_decimal_is_divisible(binary_str):

    def fibonacci_110th():
        fib_sequence = [0, 1]
        while len(fib_sequence) < 110:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[109]

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal_number = binary_to_decimal(binary_str)
    fib_110 = fibonacci_110th()
    return decimal_number % fib_110 == 0