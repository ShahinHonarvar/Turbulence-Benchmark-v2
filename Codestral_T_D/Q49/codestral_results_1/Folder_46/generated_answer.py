def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_seq = [0, 1]
    for i in range(2, 139):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return decimal % fib_seq[138] == 0