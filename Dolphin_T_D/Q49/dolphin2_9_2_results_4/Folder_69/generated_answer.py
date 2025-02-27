def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_seq = [0, 1]
    for _ in range(2, 170):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal_number % fib_seq[-1] == 0