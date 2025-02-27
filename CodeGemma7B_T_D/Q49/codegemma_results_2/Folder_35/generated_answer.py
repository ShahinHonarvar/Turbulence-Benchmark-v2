def if_decimal_is_divisible(binary):
    fib_nums = [0, 1]
    k = 2
    while k ** 2 < 10 ** len(binary):
        fib_nums.append(fib_nums[k - 1] + fib_nums[k - 2])
        k += 1
    decimal = int(binary, 2)
    if decimal in fib_nums[186:]:
        return True
    else:
        return False