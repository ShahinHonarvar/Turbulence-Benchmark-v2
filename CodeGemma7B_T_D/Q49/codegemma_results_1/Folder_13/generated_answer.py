from decimal import Decimal

def F(n):
    if n <= 1:
        return n
    return F(n - 1) + F(n - 2)

def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    nth = 174
    while True:
        fib_number = F(nth)
        if (fib_number - decimal_int) % 2 == 0:
            return True
        nth += 1