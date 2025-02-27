def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_value = int(binary_string, 2)
    forty_eighth_fib = fibonacci(48)
    return decimal_value % forty_eighth_fib == 0