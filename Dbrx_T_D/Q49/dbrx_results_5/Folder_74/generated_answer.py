def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fib_sequence = [0, 1]
    while fib_sequence[-1] < decimal_integer:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_integer % fib_sequence[165] == 0