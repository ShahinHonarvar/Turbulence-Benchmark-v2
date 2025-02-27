def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal_num = int(binary_str, 2)
    seventh_fib_num = fibonacci(7)
    return decimal_num % seventh_fib_num == 0