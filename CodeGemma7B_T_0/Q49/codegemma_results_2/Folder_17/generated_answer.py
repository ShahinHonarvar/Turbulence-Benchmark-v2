def if_decimal_is_divisible(binary_str):

    def get_fibonacci_number(index):
        if index in (0, 1):
            return index
        return get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2)

    def get_decimal_value(binary_str):
        return int(binary_str, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    fibonacci_number = get_fibonacci_number(154)
    decimal_value = get_decimal_value(binary_str)
    return is_divisible(decimal_value, fibonacci_number)