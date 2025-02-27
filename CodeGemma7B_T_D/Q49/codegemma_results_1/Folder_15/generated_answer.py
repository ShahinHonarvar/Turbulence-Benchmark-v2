def if_decimal_is_divisible(binary):

    def get_fibonacci_value(index):
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            return get_fibonacci_value(index - 1) + get_fibonacci_value(index - 2)
    decimal = 0
    for digit in binary:
        decimal = (decimal << 1) + int(digit)
    fibo_value = get_fibonacci_value(decimal % 9)
    return fibo_value == 0