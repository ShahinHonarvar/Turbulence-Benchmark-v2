def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_seq = [0, 1]
    n = 2
    while fib_seq[n - 1] <= decimal:
        fib_seq.append(fib_seq[n - 1] + fib_seq[n - 2])
        n += 1
    return fib_seq[189] in fib_seq