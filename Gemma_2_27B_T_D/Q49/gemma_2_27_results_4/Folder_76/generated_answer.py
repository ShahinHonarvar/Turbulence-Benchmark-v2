def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 188:
        next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fibonacci)
    return decimal % fibonacci_numbers[187] == 0