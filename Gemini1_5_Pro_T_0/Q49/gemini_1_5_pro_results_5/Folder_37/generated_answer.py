def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    for i in range(2, 46):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    forty_sixth_fibonacci_number = fibonacci_numbers[45]
    if decimal_representation % forty_sixth_fibonacci_number == 0:
        return True
    else:
        return False