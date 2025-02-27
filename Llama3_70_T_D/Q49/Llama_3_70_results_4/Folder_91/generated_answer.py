def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 6:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal = int(binary_str, 2)
    return decimal % fibonacci_numbers[5] == 0