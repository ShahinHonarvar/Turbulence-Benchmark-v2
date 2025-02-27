def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[n - 1]

def if_decimal_is_divisible(binary_repr):
    decimal_number = int(binary_repr, 2)
    fib_number = fibonacci_sequence(13)
    return decimal_number % fib_number == 0