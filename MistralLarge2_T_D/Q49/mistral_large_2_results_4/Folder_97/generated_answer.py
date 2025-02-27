def fibonacci(n):
    fib_values = [0, 1]
    while len(fib_values) <= n:
        fib_values.append(fib_values[-1] + fib_values[-2])
    return fib_values[n]

def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_114 = fibonacci(114)
    return decimal_value % fib_114 == 0