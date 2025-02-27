def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    sequence = [0, 1]
    for i in range(2, 28):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    if decimal_number % sequence[-1] == 0:
        return True
    else:
        return False