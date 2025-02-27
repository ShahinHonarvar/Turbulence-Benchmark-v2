def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    sequence = [0, 1]
    while len(sequence) < 168:
        sequence.append(sequence[-1] + sequence[-2])
    return decimal % sequence[-1] == 0