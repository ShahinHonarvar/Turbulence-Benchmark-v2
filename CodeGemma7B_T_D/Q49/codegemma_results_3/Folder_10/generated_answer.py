def if_decimal_is_divisible(value):

    def fibonacci(value):
        if value in (0, 1):
            return 1
        return fibonacci(value - 1) + fibonacci(value - 2)
    decimal = 0
    multiplier = 1
    for bit in reversed(value):
        decimal += multiplier * int(bit)
        multiplier *= 2
    position = 1
    nth = fibonacci(position)
    while nth <= decimal:
        if nth % decimal == 0:
            return True
        position += 1
        nth = fibonacci(position)
    return False