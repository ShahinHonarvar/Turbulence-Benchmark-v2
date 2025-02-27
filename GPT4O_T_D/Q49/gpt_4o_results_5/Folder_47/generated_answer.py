def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    for i in range(2, 95):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    target_fibo = fibonacci_numbers[94]
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fibo == 0