def if_decimal_is_divisible(binary_string):

    def fib(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal = int(binary_string, 2)
    return decimal % fib(84) == 0