def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for _ in range(2, 136):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    dec_value = int(binary_str, 2)
    return dec_value % fib_numbers[135] == 0