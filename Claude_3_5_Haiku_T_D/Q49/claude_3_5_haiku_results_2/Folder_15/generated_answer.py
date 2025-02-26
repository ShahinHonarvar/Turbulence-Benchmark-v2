def if_decimal_is_divisible(binary_string):

    def decimal_from_binary(binary):
        return int(binary, 2)

    def fibonacci_9th():
        fib = [0, 1]
        for _ in range(7):
            fib.append(fib[-1] + fib[-2])
        return fib[8]
    decimal_value = decimal_from_binary(binary_string)
    divisor = fibonacci_9th()
    return decimal_value % divisor == 0