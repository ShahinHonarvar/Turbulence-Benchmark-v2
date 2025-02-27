def if_decimal_is_divisible(binary_representation):
    first_number = 0
    second_number = 1
    position = 2
    fibonacci_number = 0
    try:
        int(binary_representation, 2)
    except ValueError:
        return False
    binary_representation_length = len(binary_representation)
    for digit in range(binary_representation_length - 1):
        temp_number = int(binary_representation[digit], 2)
        if temp_number >= 2:
            return False
        binary_representation = binary_representation[1:]
        fibonacci_number = first_number + second_number
        first_number = second_number
        second_number = fibonacci_number
        if fibonacci_number % position == 0 and fibonacci_number / position >= 199:
            return True
        position += 1
    temp_number = int(binary_representation, 2)
    if temp_number >= 2:
        return False
    fibonacci_number = first_number + second_number
    if fibonacci_number % position == 0 and fibonacci_number / position >= 199:
        return True
    return False