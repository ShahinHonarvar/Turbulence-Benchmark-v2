def if_decimal_is_divisible(binary_string):

    def fibonacci_sequence(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n - 1]
    decimal_number = int(binary_string, 2)
    fib_179 = fibonacci_sequence(179)
    return decimal_number % fib_179 == 0