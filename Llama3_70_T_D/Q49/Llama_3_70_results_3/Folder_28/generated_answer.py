def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def binary_to_decimal(binary_string):
        decimal = 0
        for i in range(len(binary_string)):
            decimal += int(binary_string[i]) * 2 ** (len(binary_string) - i - 1)
        return decimal
    decimal = binary_to_decimal(binary_string)
    fib_104 = fibonacci(104)[-1]
    return decimal % fib_104 == 0