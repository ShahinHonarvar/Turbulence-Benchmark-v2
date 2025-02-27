def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[-1]
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci(46) == 0