def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] + fibonacci_numbers[-2] < decimal_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if decimal_number % fibonacci_numbers[-19] == 0:
        return True
    else:
        return False