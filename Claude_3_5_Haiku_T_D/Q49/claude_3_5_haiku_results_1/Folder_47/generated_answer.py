def if_decimal_is_divisible(binary_str):

    def fibonacci_94():
        fib_sequence = [0, 1]
        while len(fib_sequence) < 95:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[94]
    decimal_num = int(binary_str, 2)
    fib_94 = fibonacci_94()
    return decimal_num % fib_94 == 0