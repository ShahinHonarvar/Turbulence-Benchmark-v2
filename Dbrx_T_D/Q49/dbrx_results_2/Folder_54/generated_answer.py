def is_fibonacci(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs((phi ** n - psi ** n) / 5 ** 0.5) < 1e-10

def to_decimal(binary_string):
    return int(binary_string, 2)

def fib_number(index):
    fib_sequence = [0, 1]
    while len(fib_sequence) < index:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[index - 1]

def is_divisible_by_fibonacci(binary_string):
    decimal_number = to_decimal(binary_string)
    fib_number_to_check = fib_number(34)
    return decimal_number % fib_number_to_check == 0