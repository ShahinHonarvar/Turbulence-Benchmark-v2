def if_decimal_is_divisible(binary_rep):
    decimal, i = (0, 0)
    for digit in binary_rep:
        decimal = decimal * 2 + int(digit)
    fibonacci_nums = [0, 1]
    for _ in range(2, 99):
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    fibonacci_99 = fibonacci_nums[-1]
    return decimal % fibonacci_99 == 0