def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for _ in range(2, 86):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fibonacci_85th = fib_numbers[85]
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_85th == 0