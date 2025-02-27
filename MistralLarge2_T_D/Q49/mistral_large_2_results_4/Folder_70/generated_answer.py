def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        fib = [0, 1]
        for _ in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci(137) == 0