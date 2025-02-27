def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) <= n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal_value = int(binary_str, 2)
    fib_20 = fibonacci(20)
    return decimal_value % fib_20 == 0