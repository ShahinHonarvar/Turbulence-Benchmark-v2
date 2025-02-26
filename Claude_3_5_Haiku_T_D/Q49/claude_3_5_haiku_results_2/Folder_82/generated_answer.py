def if_decimal_is_divisible(binary_str):

    def fibonacci_99():
        fib = [0, 1]
        while len(fib) < 99:
            fib.append(fib[-1] + fib[-2])
        return fib[98]

    def binary_to_decimal(binary):
        return int(binary, 2)
    divisor = fibonacci_99()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % divisor == 0