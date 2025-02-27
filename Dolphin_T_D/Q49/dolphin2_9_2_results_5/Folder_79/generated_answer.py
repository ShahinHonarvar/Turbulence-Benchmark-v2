def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) < 13:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return decimal % fib_numbers[12] == 0