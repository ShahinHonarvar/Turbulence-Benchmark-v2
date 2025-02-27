def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fib_n = fib(17)
    return decimal % fib_n == 0