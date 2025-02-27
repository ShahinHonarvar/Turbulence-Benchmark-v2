def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 135:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fibonacci_135th = fib_sequence[135]
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_135th == 0