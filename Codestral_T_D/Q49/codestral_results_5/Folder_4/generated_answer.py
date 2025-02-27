def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_nums = [0, 1]
    for i in range(2, 119):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    fib_118 = fib_nums[118]
    return decimal % fib_118 == 0