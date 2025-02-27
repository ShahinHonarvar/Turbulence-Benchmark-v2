def if_decimal_is_divisible(binary_string):
    fib_numbers = [0, 1]
    while len(fib_numbers) < 14:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    decimal_representation = int(binary_string, 2)
    return decimal_representation % fib_numbers[13] == 0