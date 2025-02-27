def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    previous = 0
    current = 1
    for _ in range(94):
        previous, current = (current, previous + current)
    return decimal % current == 0