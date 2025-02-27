def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_seq = [0, 1]
    fib_index = 2
    while fib_index < decimal:
        fib_seq.append(fib_seq[fib_index - 1] + fib_seq[fib_index - 2])
        fib_index += 1
    fib_85 = fib_seq[84]
    return decimal % fib_85 == 0