def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n + 1:
            fib.append(fib[-2] + fib[-1])
        return fib[n]
    dec = int(binary_string, 2)
    fib_198 = fibonacci(198)
    return dec % fib_198 == 0