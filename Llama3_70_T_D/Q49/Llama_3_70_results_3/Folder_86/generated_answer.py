def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n + 1:
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal = int(binary_string, 2)
    fib_135 = fibonacci(135)
    return decimal % fib_135 == 0