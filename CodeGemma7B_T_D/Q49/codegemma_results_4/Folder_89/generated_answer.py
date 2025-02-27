def if_decimal_is_divisible(binary_string):
    fib_index = 2
    fib_term = 2
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 126:
        fib_term = fib_sequence[fib_index - 1] + fib_sequence[fib_index - 2]
        fib_sequence.append(fib_term)
        fib_index += 1
    binary_integer = int(binary_string, 2)
    for num in fib_sequence:
        if num > binary_integer:
            break
        if num == binary_integer:
            return True
    return False