def is_fibonacci(n):
    return (5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fib_188_divisible(num):
    fib_sequence = fibonacci_sequence(188)
    decimal_num = int(num, 2)
    if decimal_num % fib_sequence[-1] == 0:
        return True
    else:
        return False