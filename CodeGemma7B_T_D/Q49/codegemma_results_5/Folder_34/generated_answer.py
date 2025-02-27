def if_decimal_is_divisible(bin_str):
    decimal_int = int(bin_str, 2)
    fibonacci_24 = fib(24)
    return decimal_int % fibonacci_24 == 0

def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)