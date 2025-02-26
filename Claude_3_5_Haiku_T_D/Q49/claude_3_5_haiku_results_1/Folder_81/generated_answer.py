def if_decimal_is_divisible(binary_str):

    def fibonacci_97th():
        fib_seq = [0, 1]
        while len(fib_seq) <= 97:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[97]
    decimal_num = int(binary_str, 2)
    fib_97 = fibonacci_97th()
    return decimal_num % fib_97 == 0