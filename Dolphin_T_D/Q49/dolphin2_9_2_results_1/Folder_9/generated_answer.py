def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_seq = [0, 1]
    for i in range(2, 69):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if decimal % fib_seq[68] == 0:
        return True
    else:
        return False