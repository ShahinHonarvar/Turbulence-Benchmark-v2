def is_fibonacci(n):
    return (5 * n * n + 4) % 5 == 0 or (5 * n * n - 4) % 5 == 0

def fibonacci():
    n, fib = (0, 0)
    while True:
        if is_fibonacci(n):
            yield fib
            fib = 0
            n += 1
        else:
            fib += 5 * n - 1

def decimal_to_binary_string(n):
    return bin(n)[2:]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    for i in range(80):
        fibonacci_number = next(fibonacci())
        if fibonacci_number > decimal:
            return decimal % fibonacci_number == 0
    return False