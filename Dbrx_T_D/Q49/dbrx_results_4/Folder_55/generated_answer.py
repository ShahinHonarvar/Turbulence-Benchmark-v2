def if_decimal_is_divisible(binary_string):
    decimal_number = 0
    for i in range(len(binary_string)):
        decimal_number += int(binary_string[i]) * 2 ** (len(binary_string) - i - 1)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] + fibonacci_numbers[-2] < decimal_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if decimal_number % fibonacci_numbers[38] == 0:
        return True
    else:
        return False