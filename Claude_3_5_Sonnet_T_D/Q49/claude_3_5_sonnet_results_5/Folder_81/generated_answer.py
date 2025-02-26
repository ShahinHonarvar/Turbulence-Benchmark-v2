def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n - 1]
    decimal = int(binary_str, 2)
    fib_97 = fibonacci(97)
    return decimal % fib_97 == 0