def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num % fib(109) == 0