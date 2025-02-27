def if_decimal_is_divisible(binary_string):

    def decimal_from_binary(binary_string):
        decimal = 0
        for digit in binary_string:
            decimal = decimal * 2 + int(digit)
        return decimal

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[i - 1] + fib[i - 2])
            return fib[n]
    return decimal_from_binary(binary_string) % fibonacci(99) == 0