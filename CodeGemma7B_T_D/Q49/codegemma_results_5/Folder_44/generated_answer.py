def if_decimal_is_divisible(binary_representation_str):
    decimal_int = int(binary_representation_str, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 160:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    if decimal_int % fibonacci_numbers[159] == 0:
        return True
    else:
        return False