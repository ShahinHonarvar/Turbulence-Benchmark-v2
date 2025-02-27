def if_decimal_is_divisible(binary_string):
    digits = binary_string[::-1]
    decimal = 0
    for i, digit in enumerate(digits):
        decimal += int(digit) * 2 ** i
    fibonacci_number = 1
    for _ in range(185):
        fibonacci_number, _ = fibonacci_number + decimal % fibonacci_number
    return decimal % fibonacci_number == 0