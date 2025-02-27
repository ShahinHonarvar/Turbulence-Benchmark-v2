def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for _ in range(2, 95):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    num = int(binary_str, 2)
    return num % fib_numbers[94] == 0