def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        for _ in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_number = int(binary_string, 2)
    fib_110 = fibonacci(110)
    return decimal_number % fib_110 == 0