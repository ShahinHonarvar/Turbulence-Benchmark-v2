def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fib_sequence = [0, 1]
    for i in range(2, 9):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    ninth_num = fib_sequence[8]
    return decimal_num % ninth_num == 0