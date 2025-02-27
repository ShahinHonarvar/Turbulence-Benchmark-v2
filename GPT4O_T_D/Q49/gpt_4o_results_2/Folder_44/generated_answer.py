def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    while len(fib_numbers) <= 159:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    number = int(binary_str, 2)
    return number % fib_numbers[159] == 0