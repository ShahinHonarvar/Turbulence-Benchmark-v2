def if_decimal_is_divisible(binary_str):

    def fibonacci_10th():
        fib = [0, 1]
        while len(fib) < 10:
            fib.append(fib[-1] + fib[-2])
        return fib[9]
    decimal_num = int(binary_str, 2)
    tenth_fibonacci = fibonacci_10th()
    return decimal_num % tenth_fibonacci == 0