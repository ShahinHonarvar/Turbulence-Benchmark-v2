def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib_numbers = [0, 1]
    while len(fib_numbers) < 127:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return n % fib_numbers[126] == 0