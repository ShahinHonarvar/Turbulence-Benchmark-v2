def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal = int(bin_str, 2)
    return decimal % fibonacci(104) == 0