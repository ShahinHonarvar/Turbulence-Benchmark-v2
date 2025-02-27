def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]
    decimal = int(binary_str, 2)
    fib_64th = fibonacci(64)
    return decimal % fib_64th == 0