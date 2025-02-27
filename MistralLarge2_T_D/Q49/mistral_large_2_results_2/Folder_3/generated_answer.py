def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[n]
    decimal_value = int(binary_str, 2)
    fib_35 = fibonacci(35)
    return decimal_value % fib_35 == 0