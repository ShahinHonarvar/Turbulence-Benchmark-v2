def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    N = 189
    fib_seq = [0, 1]
    for i in range(3, N + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    fib_189 = fib_seq[N - 1]
    return fib_189 != 0 and decimal % fib_189 == 0