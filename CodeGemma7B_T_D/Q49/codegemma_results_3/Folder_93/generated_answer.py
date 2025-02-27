def if_decimal_is_divisible(binary_string):
    fib_num, decimal, multiplier, i = (0, 0, 1, len(binary_string) - 1)
    for digit in binary_string:
        decimal += multiplier * int(digit)
        multiplier *= 2
    while True:
        fib_num, fib_num_next = (fib_num_next, fib_num_next + fib_num)
        if fib_num >= 59:
            break
    return decimal % fib_num == 0