def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for i in range(2, 47):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_46 = fibonacci_sequence[46]
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_46 == 0