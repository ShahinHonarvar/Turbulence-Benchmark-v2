def if_decimal_is_divisible(binary_representation):
    fib_seq = [0, 1]
    while fib_seq[-1] < 190:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal = int(binary_representation, 2)
    return decimal in fib_seq