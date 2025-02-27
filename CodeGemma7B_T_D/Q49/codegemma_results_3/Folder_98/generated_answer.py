def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    num = 0
    for i in range(2, len(binary_str)):
        num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(num)
    if int(binary_str, 2) % fib_nums[len(fib_nums) - 1] == 0:
        return True
    else:
        return False