def if_decimal_is_divisible(number):
    a, b = (0, 1)
    while len(str(b)) < len(str(number)):
        a, b = (b, a + b)
    if int(str(b)[:len(str(a))]) % 119 == 0:
        return True
    else:
        return False