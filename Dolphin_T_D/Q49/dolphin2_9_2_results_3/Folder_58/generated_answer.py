def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_num = 105
    prev, current = (0, 1)
    n = 1
    while n < fib_num:
        prev, current = (current, prev + current)
        n += 1
    return decimal % current == 0