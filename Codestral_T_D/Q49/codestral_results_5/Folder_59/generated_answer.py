def if_decimal_is_divisible(binary_rep):

    def fib(n):
        fib_seq = [0, 1]
        while len(fib_seq) <= n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal = int(binary_rep, 2)
    return decimal % fib(74) == 0