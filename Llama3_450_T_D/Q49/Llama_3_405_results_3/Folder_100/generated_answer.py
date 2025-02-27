def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n + 1:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[n]
    decimal = int(binary_string, 2)
    return decimal % fibonacci(190) == 0