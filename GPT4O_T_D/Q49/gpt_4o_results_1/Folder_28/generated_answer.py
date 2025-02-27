def if_decimal_is_divisible(binary_str):
    n = 104
    fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fibonacci_104th = fib_seq[n]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_104th == 0