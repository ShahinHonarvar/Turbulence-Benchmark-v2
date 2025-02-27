def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal_number = int(binary_rep, 2)
    fifteenth_fibonacci_number = fibonacci(15)
    return decimal_number % fifteenth_fibonacci_number == 0