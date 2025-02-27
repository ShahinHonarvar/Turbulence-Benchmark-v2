def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    def fibo(num):
        fib_seq = [0, 1]
        while len(fib_seq) <= num:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[num]
    fib_114 = fibo(113)
    if decimal % fib_114 == 0:
        return True
    else:
        return False