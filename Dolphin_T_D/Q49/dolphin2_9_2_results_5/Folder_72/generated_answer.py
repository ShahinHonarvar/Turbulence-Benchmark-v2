def if_decimal_is_divisible(binary_int):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 175:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal_int = int(binary_int, 2)
    return decimal_int % fibonacci_numbers[174] == 0