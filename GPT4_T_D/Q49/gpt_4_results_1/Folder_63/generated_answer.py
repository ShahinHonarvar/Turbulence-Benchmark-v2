def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    for i in range(2, 146):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    decimal = int(bin_str, 2)
    if decimal % fib_seq[144] == 0:
        return True
    else:
        return False