def if_decimal_is_divisible(bin_str):

    def fib_generator():
        f, s = (0, 1)
        while True:
            yield f
            f, s = (s, f + s)
    fib = fib_generator()
    nth = 190
    dec_int = int(bin_str, 2)
    found = False
    for _ in range(nth):
        num = next(fib)
        if num == dec_int:
            found = True
            break
    return found