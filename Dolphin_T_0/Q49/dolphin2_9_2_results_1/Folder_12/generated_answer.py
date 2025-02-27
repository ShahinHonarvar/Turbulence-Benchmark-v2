def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)

    def fibonacci(n):
        fib_values = [0, 1]
        while len(fib_values) < n:
            fib_values.append(fib_values[-1] + fib_values[-2])
        return fib_values[n - 1]
    return decimal_number % fibonacci(66) == 0