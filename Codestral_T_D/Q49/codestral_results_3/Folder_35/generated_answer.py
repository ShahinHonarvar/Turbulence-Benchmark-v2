def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_num = int(binary_str, 2)
    fib_187 = fibonacci(187)
    return decimal_num % fib_187 == 0