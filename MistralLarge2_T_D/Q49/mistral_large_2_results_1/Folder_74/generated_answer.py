def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        for _ in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal_num = int(binary_str, 2)
    fib_166 = fibonacci(166)
    return decimal_num % fib_166 == 0