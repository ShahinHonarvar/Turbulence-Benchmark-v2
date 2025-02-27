def if_decimal_is_divisible(binary_representation):

    def fibonacci_187():
        fib_seq = [0, 1]
        while len(fib_seq) < 187:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[187]
    decimal = int(binary_representation, 2)
    return decimal % fibonacci_187() == 0