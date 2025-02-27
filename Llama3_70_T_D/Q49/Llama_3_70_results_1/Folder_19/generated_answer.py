def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal = int(binary_str, 2)
    return decimal % fibonacci(28) == 0