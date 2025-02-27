def if_decimal_is_divisible(binary_representation):
    binary_representation_as_int = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] <= binary_representation_as_int:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    for fibonacci_number in fibonacci_sequence:
        if fibonacci_number > binary_representation_as_int:
            break
        if fibonacci_number % 45 == 0:
            return True
    return False