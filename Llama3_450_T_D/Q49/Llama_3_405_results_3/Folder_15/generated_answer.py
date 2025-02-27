def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[-1]
    divisor = fibonacci(9)
    decimal = int(binary_str, 2)
    return decimal % divisor == 0