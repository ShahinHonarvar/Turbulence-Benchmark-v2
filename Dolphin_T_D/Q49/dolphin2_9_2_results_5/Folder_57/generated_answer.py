def if_decimal_is_divisible(binary_rep):
    num_in_fibonacci = 80
    fibonacci_sequence = [0, 1]
    for i in range(2, num_in_fibonacci + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    divider = fibonacci_sequence[num_in_fibonacci - 1]
    decimal = 0
    for digit in binary_rep:
        decimal = decimal * 2 + int(digit)
    return decimal % divider == 0