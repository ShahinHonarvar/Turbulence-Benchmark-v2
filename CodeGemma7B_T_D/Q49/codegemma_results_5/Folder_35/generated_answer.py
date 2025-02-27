def if_decimal_is_divisible(number):
    a, b = (0, 1)
    for i in range(187):
        if number == '0':
            number = 1
        elif number == '1':
            number = 0
        else:
            return None
        a, b = (b, a + b)
    return number % b == 0