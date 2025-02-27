def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal = binary_to_decimal(binary_string)
    fib_190 = fibonacci(190)
    return decimal % fib_190 == 0