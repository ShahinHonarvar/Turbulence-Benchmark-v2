def if_decimal_is_divisible(bin_str):

    def generate_fibonacci():
        fib_nums = [0, 1]
        while True:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
            yield fib_nums[-1]
    fib_gen = generate_fibonacci()
    decimal_num = 0
    for digit in bin_str:
        decimal_num = decimal_num << 1 | int(digit)
    next_fib = next(fib_gen)
    while next_fib < decimal_num:
        next_fib = next(fib_gen)
    return next_fib % decimal_num == 0