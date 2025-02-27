def if_decimal_is_divisible(binary_str):

    def get_decimal_value(binary_str):
        decimal_value = 0
        power = len(binary_str) - 1
        for digit in binary_str:
            if digit == '1':
                decimal_value += 2 ** power
            power -= 1
        return decimal_value

    def get_fibonacci_value(n):
        if n <= 1:
            return n
        return get_fibonacci_value(n - 1) + get_fibonacci_value(n - 2)
    binary_int = get_decimal_value(binary_str)
    fibonacci_189 = get_fibonacci_value(189)
    return binary_int % fibonacci_189 == 0