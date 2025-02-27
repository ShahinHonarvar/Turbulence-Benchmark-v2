def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    if fib(68) != 0 and decimal % fib(68) == 0:
        return True
    else:
        return False