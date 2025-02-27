def if_decimal_is_divisible(binary_str):

    def fibonacci_nth(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    decimal_number = int(binary_str, 2)
    fib_68th = fibonacci_nth(68)
    return decimal_number % fib_68th == 0