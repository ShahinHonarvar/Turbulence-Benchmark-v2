def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    for _ in range(117):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    target_fibonacci = fibonacci_numbers[119]
    decimal_value = int(binary_str, 2)
    return decimal_value % target_fibonacci == 0