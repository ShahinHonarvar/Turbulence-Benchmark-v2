def if_decimal_is_divisible(binary_repr):
    fib_nums = [0, 1]
    while len(fib_nums) < 44:
        fib_nums.append(fib_nums[-2] + fib_nums[-1])
    decimal_num = int(binary_repr, 2)
    return decimal_num % fib_nums[-1] == 0