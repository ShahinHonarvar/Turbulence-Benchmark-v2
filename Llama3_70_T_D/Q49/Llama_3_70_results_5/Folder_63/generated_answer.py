def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[-1]
    decimal = int(binary_string, 2)
    return decimal % fibonacci(144) == 0