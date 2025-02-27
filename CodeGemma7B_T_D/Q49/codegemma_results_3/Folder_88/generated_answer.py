def if_decimal_is_divisible(binary_string):
    if not binary_string:
        return False
    decimal_number = int(binary_string, 2)
    fib_sequence = [0]
    if len(binary_string) >= 4:
        for i in range(48):
            fib_sequence.append(fib_sequence[i] + fib_sequence[i + 1])
        if decimal_number % fib_sequence[48] == 0:
            return True
    return False