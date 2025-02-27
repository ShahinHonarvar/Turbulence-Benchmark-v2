def if_decimal_is_divisible(binary):

    def fib(n):
        if n < 3:
            return 1
        else:
            return fib(n - 2) + fib(n - 1)
    Nth = list(str(fib(175)))
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    if decimal % int(''.join(Nth)) == 0:
        return True
    else:
        return False