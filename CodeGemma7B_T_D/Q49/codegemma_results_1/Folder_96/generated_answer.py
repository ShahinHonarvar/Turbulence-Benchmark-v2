def if_decimal_is_divisible(binary_representation):
    fib_nums = [0]
    binary_num = int(binary_representation, 2)
    for i in range(1, 50):
        fib_num = fib_nums[i - 1] + fib_nums[i - 2]
        fib_nums.append(fib_num)
        if fib_num == binary_num:
            return True
    return False