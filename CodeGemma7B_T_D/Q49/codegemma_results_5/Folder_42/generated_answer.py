def is_decimal_divisible_by_146th_fibonacci_number(binary_string):
    fibonacci_numbers = set([0, 1])
    for i in range(2, len(binary_string)):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.add(next_number)
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibonacci_numbers[146] == 0:
        return True
    else:
        return False