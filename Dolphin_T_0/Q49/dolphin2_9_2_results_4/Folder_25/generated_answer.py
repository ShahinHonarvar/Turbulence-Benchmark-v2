def if_decimal_is_divisible(binary):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 19:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal = int(binary, 2)
    return decimal % fibonacci_numbers[18] == 0