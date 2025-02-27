def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_seq = [0, 1]
    for _ in range(77):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    seventy_eighth_fibonacci_num = fib_seq[77]
    decimal_num = int(binary_str, 2)
    return decimal_num % seventy_eighth_fibonacci_num == 0