def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 16):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    sixteenth_fibonacci_number = fibonacci_numbers[15]
    if decimal_representation % sixteenth_fibonacci_number == 0:
        return True
    else:
        return False