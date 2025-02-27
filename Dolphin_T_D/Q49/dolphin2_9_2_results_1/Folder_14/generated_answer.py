def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 27:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_num = fib_sequence[26]
    if n % fib_num == 0:
        return True
    else:
        return False