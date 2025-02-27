def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n < 1:
            raise ValueError('Invalid input. n must be greater than or equal to 1.')
        return fibonacci(n - 1)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, bit in enumerate(binary_representation):
            decimal_value += int(bit) * 2 ** i
        return decimal_value

    def is_divisible(decimal_value, divisor):
        return decimal_value % divisor == 0
    binary_representation = binary_representation.strip()
    if not binary_representation or not binary_representation.startswith('0'):
        raise ValueError("Invalid input. Binary representation must start with '0'.")
    nth_fibonacci = get_nth_fibonacci(179)
    decimal_value = get_decimal_value(binary_representation)
    return is_divisible(decimal_value, nth_fibonacci)