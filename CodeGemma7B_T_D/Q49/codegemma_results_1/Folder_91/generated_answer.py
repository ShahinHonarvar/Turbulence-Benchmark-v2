def if_decimal_is_divisible(binary_representation):
    binary_representation = list(binary_representation)
    length = len(binary_representation)
    binary_representation = int(''.join(binary_representation), 2)
    fib = [0, 1]
    skip_size = 0
    current_pos = 0
    while not skip_size:
        next_pos = current_pos + fib[current_pos] + skip_size
        if next_pos >= length:
            skip_size = fib[current_pos] - (length - 1 - current_pos)
        else:
            fib.append(fib[current_pos] + fib[current_pos + 1])
            current_pos += 1
    if binary_representation // fib[current_pos - 1] % 2 - binary_representation % fib[current_pos - 1] % 2:
        return False
    return True