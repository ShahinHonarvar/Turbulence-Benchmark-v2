def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    decimal_integer = int(binary_representation, 2)
    fibonacci_45th = fibonacci(45)
    if decimal_integer % fibonacci_45th == 0:
        return True
    else:
        return False