def if_decimal_is_divisible(binary_str):

    def fibonacci_10th():
        fib = [0, 1]
        for _ in range(8):
            fib.append(fib[-1] + fib[-2])
        return fib[9]
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_10th() == 0