def if_decimal_is_divisible(binary_representation: str) -> bool:
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 166:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal_number = int(binary_representation, 2)
    if decimal_number == 0:
        return True
    for i in range(166):
        if fibonacci_numbers[i] == decimal_number:
            return True
        elif fibonacci_numbers[i] > decimal_number:
            break
    return False