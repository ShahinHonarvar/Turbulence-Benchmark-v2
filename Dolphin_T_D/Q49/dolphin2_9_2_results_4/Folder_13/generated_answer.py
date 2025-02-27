def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib174 = (pow(1 + pow(5, 0.5), 173) - pow(1 - pow(5, 0.5), 173)) / (pow(5, 0.5) * 2)
    if decimal % int(fib174) == 0:
        return True
    else:
        return False