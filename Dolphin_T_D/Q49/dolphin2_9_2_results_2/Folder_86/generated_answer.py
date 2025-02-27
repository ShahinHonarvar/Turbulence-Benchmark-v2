def if_decimal_is_divisible(bin_str):
    bin_num = int(bin_str, 2)
    a = 0
    b = 1
    fib_seq = []
    for _ in range(134):
        c = a + b
        a = b
        b = c
        fib_seq.append(a)
    return bin_num % fib_seq[134] == 0