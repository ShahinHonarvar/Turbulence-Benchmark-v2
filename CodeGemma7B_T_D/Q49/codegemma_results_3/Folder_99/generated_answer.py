def if_decimal_is_divisible(binary):
    length = len(binary)
    fib_nums = [0, 1]
    while fib_nums[-1] < 2 ** length + 1:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    index = binary.index('1')
    return int(binary[0:index], 2) in fib_nums[2::2] and int(binary[index:], 2) % fib_nums[108] == 0