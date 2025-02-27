def if_decimal_is_divisible(binary_number: str) -> bool:
    binary_number = int(binary_number, 2)
    fib_sequence = [0, 1]
    for i in range(2, 80 + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    if binary_number % fib_sequence[80] == 0:
        return True
    else:
        return False