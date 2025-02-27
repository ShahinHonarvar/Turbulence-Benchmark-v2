def if_decimal_is_divisible(binary):
    return bin(127 * fib(int(binary, 2))).count('1') % 2 == 0

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)