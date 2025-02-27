def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)

    def fibonacci(n):
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[n - 1]
    fib_144th = fibonacci(144)
    return decimal % fib_144th == 0