def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    decimal_number = int(binary_string, 2)
    fib_120 = fibonacci(120)
    return decimal_number % fib_120 == 0