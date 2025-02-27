def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    n = 105
    a = 0
    b = 1
    fib_sequence = []
    while len(fib_sequence) < n:
        next_num = a + b
        fib_sequence.append(next_num)
        a = b
        b = next_num
    return decimal % fib_sequence[-1] == 0