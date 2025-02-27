def if_decimal_is_divisible(binary_rep):

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n + 1:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal_num = int(binary_rep, 2)
    return decimal_num % fibonacci(198) == 0