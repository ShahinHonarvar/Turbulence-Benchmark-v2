def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_numbers = [0, 1]
    for _ in range(2, 28):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return decimal_number % fib_numbers[27] == 0