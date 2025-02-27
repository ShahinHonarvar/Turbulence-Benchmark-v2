def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)
    decimal = binary_to_decimal(binary_string)
    fib_90 = fibonacci(90)[-1]
    return decimal % fib_90 == 0