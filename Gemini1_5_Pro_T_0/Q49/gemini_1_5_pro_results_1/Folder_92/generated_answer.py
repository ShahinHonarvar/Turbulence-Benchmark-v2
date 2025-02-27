def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 7):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    seventh_fibonacci_number = fibonacci_numbers[6]
    if decimal_representation % seventh_fibonacci_number == 0:
        return True
    else:
        return False