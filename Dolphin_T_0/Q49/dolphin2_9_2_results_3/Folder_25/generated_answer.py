def if_decimal_is_divisible(binary):
    n = 2
    fib_sequence = [0, 1]
    while n < 19:
        fib_next = fib_sequence[n - 2] + fib_sequence[n - 1]
        fib_sequence.append(fib_next)
        n += 1
    decimal_rep = int(binary, 2)
    if decimal_rep % fib_sequence[18] == 0:
        return True
    else:
        return False