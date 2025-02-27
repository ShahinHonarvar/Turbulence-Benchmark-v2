def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_binary(decimal):
        if decimal == 0:
            return '0'
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_to_decimal = int(binary, 2)
    nth_fibonacci = get_nth_fibonacci(178)
    return is_divisible(binary_to_decimal, nth_fibonacci)