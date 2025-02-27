def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    for _ in range(2, 196):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    fib_195 = fibonacci_numbers[195]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_195 == 0