def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < decimal_integer:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    target_fibonacci_number = fibonacci_numbers[120]
    return decimal_integer % target_fibonacci_number == 0