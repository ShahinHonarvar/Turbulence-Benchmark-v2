def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 176:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_176 = fib_seq[175]
    if decimal_integer % fib_176 == 0:
        return True
    else:
        return False