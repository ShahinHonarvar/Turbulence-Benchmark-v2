def if_decimal_is_divisible(binary_str):

    def fib(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            return fib(n - 1) + fib(n - 2)
    binary = int(binary_str, 2)
    return binary % fib(10) == 0