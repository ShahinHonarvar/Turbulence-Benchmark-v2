def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fib_seq = [0, 1]
    for i in range(2, 186 + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    if decimal_num % fib_seq[-1] == 0:
        return True
    else:
        return False