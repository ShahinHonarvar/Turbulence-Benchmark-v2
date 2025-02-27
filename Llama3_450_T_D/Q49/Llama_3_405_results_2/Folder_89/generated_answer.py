def if_decimal_is_divisible(s):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    divisor = fibonacci(126)
    decimal_integer = int(s, 2)
    return decimal_integer % divisor == 0