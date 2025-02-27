def if_decimal_is_divisible(binary_representation):
    fibonacci_numbers = [0, 1]
    for _ in range(2, 196):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    target = fibonacci_numbers[195]
    decimal_number = int(binary_representation, 2)
    return decimal_number % target == 0