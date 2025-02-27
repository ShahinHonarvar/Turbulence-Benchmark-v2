def if_decimal_is_divisible(binary_str):
    length = len(binary_str)
    fibonacci_numbers = [0]
    decimal_int = 0
    for i in range(length):
        decimal_int = decimal_int + int(binary_str[length - i - 1]) * 2 ** i
    while len(fibonacci_numbers) < 100:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    if decimal_int % fibonacci_numbers[99] == 0:
        return True
    else:
        return False