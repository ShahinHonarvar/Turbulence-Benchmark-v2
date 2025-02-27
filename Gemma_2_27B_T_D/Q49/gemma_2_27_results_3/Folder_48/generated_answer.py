def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 199:
        next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fibonacci)
    return decimal % fibonacci_numbers[198] == 0