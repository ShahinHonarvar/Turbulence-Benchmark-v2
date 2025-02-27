def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]
    decimal = int(binary_str, 2)
    fib_88 = fibonacci(88)
    return decimal % fib_88 == 0