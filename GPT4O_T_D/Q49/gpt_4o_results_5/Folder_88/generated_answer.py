def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for i in range(2, 50):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    n = int(binary_str, 2)
    return n % fib_numbers[49] == 0