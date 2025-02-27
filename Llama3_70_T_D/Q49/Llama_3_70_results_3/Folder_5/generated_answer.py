def if_decimal_is_divisible(binary_string):

    def is_divisible(n, divisor):
        return n % divisor == 0

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal_number = int(binary_string, 2)
    divisor = fibonacci(85)
    return is_divisible(decimal_number, divisor)