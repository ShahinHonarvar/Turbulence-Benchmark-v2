def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal = int(binary_representation, 2)
    divisor = fibonacci(120)
    return decimal % divisor == 0