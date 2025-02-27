def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n - 1]
    return decimal_number % fibonacci(87) == 0