def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 177:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    fib_177 = fibonacci_numbers[176]
    return decimal_num % fib_177 == 0