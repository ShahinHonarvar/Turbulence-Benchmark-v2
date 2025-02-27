def if_decimal_is_divisible(binary_string):
    a, b = (0, 1)
    fib_sequence = [0]
    for _ in range(15):
        a, b = (b, a + b)
        fib_sequence.append(b)
    decimal_number = int(binary_string, 2)
    for num in fib_sequence:
        if decimal_number % num == 0:
            return True
    return False