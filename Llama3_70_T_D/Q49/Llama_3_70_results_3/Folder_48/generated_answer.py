def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[-1]
    decimal = int(binary_str, 2)
    divisor = fibonacci(199)
    return decimal % divisor == 0