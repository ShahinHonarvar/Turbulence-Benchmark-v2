def if_decimal_is_divisible(binary_str):

    def get_fibonacci(d):
        if d == 0:
            return 0
        elif d == 1:
            return 1
        else:
            return get_fibonacci(d - 1) + get_fibonacci(d - 2)
    binary_length = len(binary_str)
    decimal_int = 0
    for i in range(binary_length):
        decimal_int += int(binary_str[binary_length - i - 1]) * 2 ** i
    sixety_ninth_fibonacci = get_fibonacci(69)
    return decimal_int % sixety_ninth_fibonacci == 0