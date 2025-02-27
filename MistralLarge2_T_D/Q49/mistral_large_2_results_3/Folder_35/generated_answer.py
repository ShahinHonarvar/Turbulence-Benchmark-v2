def if_decimal_is_divisible(binary):

    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal = int(binary, 2)
    fib_187 = fibonacci(187)
    return decimal % fib_187 == 0