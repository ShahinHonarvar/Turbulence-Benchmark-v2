def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) < 160:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fib_number = fib_numbers[160 - 1]
    return num % fib_number == 0