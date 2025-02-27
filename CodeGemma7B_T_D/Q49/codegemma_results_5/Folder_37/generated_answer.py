def if_decimal_is_divisible(binary_str):

    def fib_gen():
        x, y = (0, 1)
        while x <= INT_MAX:
            yield x
            x, y = (y, x + y)
    INT_MAX = 2 ** (len(binary_str) * 8 - 1)
    fibonacci_numbers = [i for i in fib_gen() if i <= INT_MAX]
    forty_sixth_fibonacci = fibonacci_numbers[46]
    decimal_value = int(binary_str, 2)
    return decimal_value % forty_sixth_fibonacci == 0