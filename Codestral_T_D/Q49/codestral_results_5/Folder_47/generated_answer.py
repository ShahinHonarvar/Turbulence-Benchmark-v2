def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) <= n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal = int(bin_str, 2)
    fib_94 = fibonacci(94)
    return decimal % fib_94 == 0