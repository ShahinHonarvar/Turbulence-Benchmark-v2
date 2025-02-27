def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

    def binary_to_decimal(binary_string):
        decimal = 0
        for char in binary_string:
            decimal = decimal * 2 + int(char)
        return decimal
    decimal = binary_to_decimal(binary_string)
    fib_199 = fibonacci(199)
    return decimal % fib_199 == 0