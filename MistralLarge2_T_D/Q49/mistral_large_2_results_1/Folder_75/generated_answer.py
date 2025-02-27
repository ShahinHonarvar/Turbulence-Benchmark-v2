def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        return fib[n]

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    decimal_num = binary_to_decimal(binary_str)
    fib_189 = fibonacci(189)
    return decimal_num % fib_189 == 0