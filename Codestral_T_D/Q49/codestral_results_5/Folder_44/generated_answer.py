def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n]

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_159 = fibonacci(159)
    return decimal % fib_159 == 0