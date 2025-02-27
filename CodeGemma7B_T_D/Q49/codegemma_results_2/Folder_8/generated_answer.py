def if_decimal_is_divisible(binary_str):
    decimal_num = 0
    for i, digit in enumerate(binary_str):
        decimal_num += int(digit) * 2 ** i
    fibonacci_num = ((1 + 5 ** 0.5) / 2) ** n - ((1 - 5 ** 0.5) / 2) ** n
    return decimal_num % fibonacci_num == 0