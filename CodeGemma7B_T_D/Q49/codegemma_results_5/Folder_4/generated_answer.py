def if_decimal_is_divisible(binary_representation):
    compare_number = fibonacci(118)
    decimal_number = 0
    for index, digit in enumerate(binary_representation):
        decimal_number = decimal_number + int(digit) * 2 ** index
    return decimal_number % compare_number == 0

def fibonacci(number):
    sequence = [0, 1]
    for n in range(2, number + 1):
        sequence.append(sequence[n - 1] + sequence[n - 2])
    return sequence[number]