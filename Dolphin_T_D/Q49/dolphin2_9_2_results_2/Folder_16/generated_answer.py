def if_decimal_is_divisible(binary_rep):
    fib_seq = [0, 1]
    i = 2
    while fib_seq[i - 1] <= 2 ** len(binary_rep):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        i += 1
    fib_128 = fib_seq[127]
    dec = int(binary_rep, 2)
    if fib_128 != 0 and dec % fib_128 == 0:
        return True
    else:
        return False