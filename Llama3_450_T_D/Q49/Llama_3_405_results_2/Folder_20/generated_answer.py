def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[-1]
    divisor = fibonacci(100)
    decimal = int(binary_string, 2)
    return decimal % divisor == 0