def if_decimal_is_divisible(binary_rep):
    a, b = (0, 1)
    fib_seq = [a]
    for _ in range(73):
        a, b = (b, a + b)
        fib_seq.append(a)
    num = int(binary_rep, 2)
    return num % fib_seq[-1] == 0