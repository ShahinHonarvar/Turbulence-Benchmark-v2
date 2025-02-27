def if_decimal_is_divisible(binary):
    n = 0
    fibonacci_number = 0
    while n != 125:
        fibonacci_number += n
        if n == 0:
            n = 1
        else:
            n = fibonacci_number
    decimal = int(binary, 2)
    if decimal % fibonacci_number == 0:
        return True
    else:
        return False