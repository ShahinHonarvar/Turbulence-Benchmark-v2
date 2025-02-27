def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 100:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_number = fib_seq[-1]
    if decimal % fib_number == 0:
        return True
    else:
        return False