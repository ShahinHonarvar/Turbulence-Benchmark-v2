def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n - 1]
    decimal = binary_to_decimal(binary_string)
    fourth_fib = fibonacci(4)
    return decimal % fourth_fib == 0