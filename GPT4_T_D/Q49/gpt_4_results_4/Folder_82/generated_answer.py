def if_decimal_is_divisible(binary_repr):
    decimal_repr = int(binary_repr, 2)
    fibonacci_sequence = [0, 1]
    for i in range(98):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_99th = fibonacci_sequence[-1]
    if decimal_repr % fibonacci_99th == 0:
        return True
    else:
        return False