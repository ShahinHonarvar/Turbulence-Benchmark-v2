def if_decimal_is_divisible(binary_string):
    fib_numbers = [0, 1]
    for _ in range(2, 29):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_numbers[28] == 0