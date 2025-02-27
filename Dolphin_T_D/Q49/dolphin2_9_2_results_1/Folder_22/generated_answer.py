def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 20:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_20 = fib_seq[-1]
    if decimal % fib_20 == 0:
        return True
    else:
        return False