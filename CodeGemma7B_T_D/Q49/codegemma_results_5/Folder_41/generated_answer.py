def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = fibonacci(67)
    return decimal_integer % fibonacci_number == 0

def fibonacci(index):
    fibonacci_sequence = [0, 1]
    for i in range(2, index):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return fibonacci_sequence[index - 1]