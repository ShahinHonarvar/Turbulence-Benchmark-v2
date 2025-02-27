def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 189:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fib_189 = fib_nums[-1]
    return decimal % fib_189 == 0