def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    for _ in range(2, 18):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    seventeenth_fibonacci = fibonacci_numbers[16]
    return decimal_value % seventeenth_fibonacci == 0