def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 126:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    fibonacci_126 = fibonacci_numbers[125]
    return decimal_number % fibonacci_126 == 0