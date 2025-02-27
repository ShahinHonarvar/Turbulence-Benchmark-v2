def if_decimal_is_divisible(binary_str):

    def decimal_from_binary(binary_str):
        return int(binary_str, 2)

    def fibonacci_seq(n):
        seq = [0, 1]
        while len(seq) <= n:
            seq.append(seq[-1] + seq[-2])
        return seq[n]
    number = decimal_from_binary(binary_str)
    fib_number = fibonacci_seq(116)
    return number % fib_number == 0