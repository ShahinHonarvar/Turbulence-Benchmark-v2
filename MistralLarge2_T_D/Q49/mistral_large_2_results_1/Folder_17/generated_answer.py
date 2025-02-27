def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_int = int(binary_str, 2)
    fib_154 = fibonacci(154)
    return decimal_int % fib_154 == 0