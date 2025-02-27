def if_decimal_is_divisible(binary_string):

    def get_fibonacci(n):
        if n <= 1:
            return n
        else:
            return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def convert_to_decimal(binary_string):
        decimal = 0
        power = len(binary_string) - 1
        for bit in binary_string:
            decimal += int(bit) * 2 ** power
            power -= 1
        return decimal
    decimal = convert_to_decimal(binary_string)
    fibonacci_number = get_fibonacci(107)
    return decimal % fibonacci_number == 0