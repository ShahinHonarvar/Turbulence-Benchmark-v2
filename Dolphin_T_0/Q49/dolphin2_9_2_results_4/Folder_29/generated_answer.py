def if_decimal_is_divisible(binary_string):

    def fib(n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]
    decimal = int(binary_string, 2)
    if decimal % fib(116) == 0:
        return True
    else:
        return False