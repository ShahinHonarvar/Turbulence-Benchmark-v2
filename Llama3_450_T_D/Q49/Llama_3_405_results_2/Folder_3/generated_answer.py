def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[n - 1]
    decimal_num = int(binary_str, 2)
    fib_35 = fibonacci(35)
    return decimal_num % fib_35 == 0