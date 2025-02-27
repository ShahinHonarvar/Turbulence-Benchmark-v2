def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) <= n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[n]
    decimal_num = int(binary_str, 2)
    fibonacci_97 = fibonacci(97)
    return decimal_num % fibonacci_97 == 0