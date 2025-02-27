def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    sequence = [0, 1]
    while len(sequence) < 15:
        sequence.append(sequence[-1] + sequence[-2])
    fibonacci_15th = sequence[-1]
    return decimal % fibonacci_15th == 0