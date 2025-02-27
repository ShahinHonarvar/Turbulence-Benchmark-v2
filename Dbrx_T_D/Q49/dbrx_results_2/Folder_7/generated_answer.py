def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 160
    fibonacci_sequence = [0, 1]
    while fibonacci_number < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        fibonacci_number += 1
    if decimal_integer == 160:
        return fibonacci_number % decimal_integer == 0
    else:
        return fibonacci_number % decimal_integer == 0 and decimal_integer % 160 == 0