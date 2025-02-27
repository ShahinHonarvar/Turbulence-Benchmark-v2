def is_divisible_by_fib54(binary_str):

    def fib54():
        fib_seq = [0, 1]
        while len(fib_seq) < 54:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[-1]
    decimal_num = int(binary_str, 2)
    return decimal_num % fib54() == 0