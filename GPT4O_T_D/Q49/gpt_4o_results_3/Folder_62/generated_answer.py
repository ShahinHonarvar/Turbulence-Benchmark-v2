def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    def fibonacci(n):
        if n <= 1:
            return n
        fib_numbers = [0, 1]
        for i in range(2, n + 1):
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers[-1]
    fibonacci_130 = fibonacci(130)
    return decimal_number % fibonacci_130 == 0