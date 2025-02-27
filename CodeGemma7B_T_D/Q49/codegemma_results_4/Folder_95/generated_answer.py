def if_decimal_is_divisible(binary_representation):
    fib(169)
    test = int(binary_representation, 2)
    return test % fib(169) == 0

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)