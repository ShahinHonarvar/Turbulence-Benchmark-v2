def if_decimal_is_divisible(binary):

    def decimal_from_binary(binary):
        return int(binary, 2)

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    fib_137 = fibonacci(137)[-1]
    n = decimal_from_binary(binary)
    return n % fib_137 == 0