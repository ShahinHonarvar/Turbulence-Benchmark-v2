def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_num = 48
    if fibonacci_num < 0:
        raise ValueError('Fibonacci sequence does not contain negative numbers')
    fib_sequence = [0, 1]
    while len(fib_sequence) < fibonacci_num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if decimal_integer % fib_sequence[-1] == 0:
        return True
    else:
        return False