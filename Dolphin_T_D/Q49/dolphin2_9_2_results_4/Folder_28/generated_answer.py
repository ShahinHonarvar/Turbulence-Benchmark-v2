def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[n - 1]
    return int(binary_string, 2) % fibonacci(104) == 0