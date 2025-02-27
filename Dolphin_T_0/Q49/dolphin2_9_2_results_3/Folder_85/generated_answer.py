def if_decimal_is_divisible(binary):
    n = 0
    fibonacci_45 = 0
    while n != 45:
        fibonacci_45, fibonacci_44 = (fibonacci_44, fibonacci_45 + fibonacci_44)
        n += 1
    decimal = int(binary, 2)
    return decimal % fibonacci_45 == 0