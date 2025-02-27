def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[-1]
    decimal_number = int(binary_string, 2)
    fib_number = fibonacci(28)
    return decimal_number % fib_number == 0