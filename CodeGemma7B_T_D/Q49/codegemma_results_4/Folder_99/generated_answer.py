def if_decimal_is_divisible(bit_string):

    def fibonacci(n):
        return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)

    def convert_bit_string_to_decimal(bit_string):
        return sum([int(bit) * 2 ** i for i, bit in enumerate(bit_string)][::-1])
    fib = fibonacci(108)
    dec = convert_bit_string_to_decimal(bit_string)
    return dec % fib == 0