def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    for i in range(1, 16):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    decimal = int(binary_str, 2)
    for num in fib_nums:
        if decimal % num == 0:
            return True
    return False