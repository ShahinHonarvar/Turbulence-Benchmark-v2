def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_series = [0, 1]
        for i in range(2, n + 1):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[n]
    decimal_value = int(binary_string, 2)
    fibonacci_ninth = fibonacci(9)
    return decimal_value % fibonacci_ninth == 0