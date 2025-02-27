def if_decimal_is_divisible(binary_string):

    def to_decimal(binary_string):
        decimal = 0
        for digit in binary_string:
            decimal = decimal * 2 + int(digit)
        return decimal

    def fibonacci(n):
        fib_numbers = [0, 1]
        for _ in range(2, n + 1):
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers
    binary_decimal = to_decimal(binary_string)
    fib_195 = fibonacci(195)[-1]
    return binary_decimal % fib_195 == 0