def if_decimal_is_divisible(binary_representation):
    fib_num = fib(binary_representation.count('1'))
    while fib_num % 97 != 0:
        fib_num = fib(fib_num)
    return fib_num == int(binary_representation, 2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)