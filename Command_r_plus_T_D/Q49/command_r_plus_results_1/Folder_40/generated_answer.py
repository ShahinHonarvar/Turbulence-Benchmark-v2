def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_num = 3
    fib_sequence = [0, 1, 1]
    for _ in range(fib_num):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_sequence[fib_num] == 0:
        return True
    else:
        return False