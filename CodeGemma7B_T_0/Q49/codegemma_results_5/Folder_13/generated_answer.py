def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_int(binary):
        return int(binary, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    fib_index = 174
    fib_num = fibonacci(fib_index)
    decimal = decimal_to_int(binary)
    return is_divisible(decimal, fib_num)