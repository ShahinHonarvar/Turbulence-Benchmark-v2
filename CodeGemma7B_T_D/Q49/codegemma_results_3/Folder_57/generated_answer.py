def if_decimal_is_divisible(bin_num):
    fib_num = _fib_num_creator()
    if int(bin_num, 2) % next(fib_num) == 0:
        return True
    else:
        return False

def _fib_num_creator():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)