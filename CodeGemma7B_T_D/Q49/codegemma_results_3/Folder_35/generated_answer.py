from math import sqrt

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def get_index_of_fib_binary(fib_num_binary, sequence):
    for i in range(len(sequence)):
        if sequence[i] == fib_num_binary:
            return i

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_num = fibonacci(len(binary_str))
    fib_num_binary = bin(fib_num)[2:]
    sequence = [str(i) for i in range(fib_num + 1)]
    index_in_sequence = get_index_of_fib_binary(fib_num_binary, sequence)
    if index_in_sequence % 187 == 0:
        return True
    else:
        return False