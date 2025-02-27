def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible(dec_string):
    decimal_num = int(dec_string, 2)
    fib_numbers = list(fib())
    fib_20 = fib_numbers[19]
    if decimal_num % fib_20 == 0:
        return True
    else:
        return False