def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    while len(fib_numbers) <= 110:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    target_fib = fib_numbers[110]
    decimal_value = int(binary_str, 2)
    return decimal_value % target_fib == 0