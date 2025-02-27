def if_decimal_is_divisible(binary_rep):
    decimal = 0
    for i in range(len(binary_rep)):
        if binary_rep[i] == '1':
            decimal += 2 ** i
    fib_seq = [0, 1]
    for i in range(2, 176):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return decimal % fib_seq[175] == 0