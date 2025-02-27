def if_decimal_is_divisible(binary_number_string):
    if binary_number_string == '':
        return False
    decimal_number = int(binary_number_string, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) <= 56:
        fib_numbers.append(fib_numbers[-2] + fib_numbers[-1])
    return decimal_number % fib_numbers[-1] == 0