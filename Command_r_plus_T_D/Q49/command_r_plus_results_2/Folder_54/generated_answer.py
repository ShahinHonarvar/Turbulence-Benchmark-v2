def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_num = 34
    fib_sequence = [0, 1]
    while len(fib_sequence) < fib_num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    thirty_fourth_fib_num = fib_sequence[33]
    decimal_num = int(binary_str, 2)
    return decimal_num % thirty_fourth_fib_num == 0