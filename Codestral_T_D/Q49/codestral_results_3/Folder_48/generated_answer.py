def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n + 1:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n]

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_198 = fibonacci(198)
    return decimal_num % fib_198 == 0