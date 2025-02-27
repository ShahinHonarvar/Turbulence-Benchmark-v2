def if_decimal_is_divisible(binary):

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[-1]
    decimal = int(binary, 2)
    fib_166 = fibonacci(166)
    return decimal % fib_166 == 0