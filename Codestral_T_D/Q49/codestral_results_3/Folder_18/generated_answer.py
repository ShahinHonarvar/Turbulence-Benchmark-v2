def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n - 1]
    fibonacci_number = fibonacci(199)
    return decimal_number % fibonacci_number == 0