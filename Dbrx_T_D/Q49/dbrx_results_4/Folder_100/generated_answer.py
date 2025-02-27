def if_decimal_is_divisible(bin_repr):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal_num = int(bin_repr, 2)
    return decimal_num % fibonacci(190) == 0