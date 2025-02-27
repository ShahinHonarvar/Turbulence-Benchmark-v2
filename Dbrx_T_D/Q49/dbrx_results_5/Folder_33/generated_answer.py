def if_decimal_is_divisible(bin_str):
    decimal_int = int(bin_str, 2)
    fib_sequence = [0, 1]
    current = 1
    while fib_sequence[current] < decimal_int:
        fib_sequence.append(fib_sequence[current - 1] + fib_sequence[current])
        current += 1
    if decimal_int % fib_sequence[133] == 0:
        return True
    else:
        return False