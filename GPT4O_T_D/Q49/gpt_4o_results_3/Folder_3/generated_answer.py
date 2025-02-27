def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[n]
    fibonacci_35th = fibonacci(35)
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_35th == 0