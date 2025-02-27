def if_decimal_is_divisible(s):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    divisor = fibonacci(58)
    decimal = int(s, 2)
    return decimal % divisor == 0