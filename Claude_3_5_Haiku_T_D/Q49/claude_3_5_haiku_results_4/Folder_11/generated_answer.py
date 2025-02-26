def if_decimal_is_divisible(binary_string):

    def fibonacci_16th():
        fib = [0, 1]
        while len(fib) < 16:
            fib.append(fib[-1] + fib[-2])
        return fib[15]
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_16th() == 0