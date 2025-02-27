def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 45:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal % fib_seq[45] == 0