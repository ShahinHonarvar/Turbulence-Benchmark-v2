def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def if_decimal_is_divisible(binary_string):
    fib_sequence = generate_fibonacci(75)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_sequence[74] == 0