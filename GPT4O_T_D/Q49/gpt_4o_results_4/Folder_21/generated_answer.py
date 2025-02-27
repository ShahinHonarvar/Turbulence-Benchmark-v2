def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[-1] + fib[-2])
            return fib[-1]
    fib_195 = fibonacci(195)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_195 == 0