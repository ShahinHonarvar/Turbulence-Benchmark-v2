def if_decimal_is_divisible(binary_string):

    def fibonacci(num):
        sequence = [0, 1]
        while len(sequence) <= num:
            sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])
        return sequence[num]
    decimal_number = int(binary_string, 2)
    fibonacci_180 = fibonacci(180)
    if decimal_number % fibonacci_180 == 0:
        return True
    else:
        return False