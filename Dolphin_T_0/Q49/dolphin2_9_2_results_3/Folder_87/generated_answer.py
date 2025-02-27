def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_180 = fibonacci(180)
    return decimal % fib_180 == 0