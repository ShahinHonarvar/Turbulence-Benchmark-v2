def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while True:
        next_fibonacci_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        if next_fibonacci_number > decimal_number:
            break
        fibonacci_numbers.append(next_fibonacci_number)
    return decimal_number % fibonacci_numbers[19] == 0