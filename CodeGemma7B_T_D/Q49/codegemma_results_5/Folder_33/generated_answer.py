def if_decimal_is_divisible(binary_str):
    num = 0
    for digit in binary_str:
        num = num * 2 + int(digit)
    for i, fibonacci in enumerate(fibonacci()):
        if fibonacci == 134:
            return True
        elif num % fibonacci == 0:
            return False