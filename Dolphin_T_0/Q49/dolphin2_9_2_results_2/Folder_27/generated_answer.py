def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    a, b = (0, 1)
    fib_seq = [a]
    for _ in range(87):
        a, b = (b, a + b)
        fib_seq.append(a)
    return decimal % fib_seq[86] == 0