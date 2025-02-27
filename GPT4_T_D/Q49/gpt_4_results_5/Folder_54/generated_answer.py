def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) < 34:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    if decimal % fib_numbers[33] == 0:
        return True
    else:
        return False