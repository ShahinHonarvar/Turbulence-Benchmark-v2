def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal_value = binary_to_decimal(binary_str)
    fib_90 = fibonacci(90)
    return decimal_value % fib_90 == 0