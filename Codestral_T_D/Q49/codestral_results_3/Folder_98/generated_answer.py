def fibonacci(n):
    fib_seq = [0, 1]
    for _ in range(n - 2):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[-1]

def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_14 = fibonacci(14)
    return decimal % fib_14 == 0