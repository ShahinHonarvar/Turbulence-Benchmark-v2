def if_decimal_is_divisible(binary_string):
    fib_numbers = [0, 1]
    current_number = 1
    while len(fib_numbers) < 34:
        current_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(current_number)
    decimal_number = int(binary_string, 2)
    if decimal_number % fib_numbers[34] == 0:
        return True
    else:
        return False