def if_decimal_is_divisible(binary_str):
    fib_nums = [0]
    current_num = 0
    k = 0
    while current_num <= int(binary_str, 2):
        k += 1
        current_num = fib_nums[k - 1] + fib_nums[k]
        fib_nums.append(current_num)
    divisible_index = fib_nums.index(int(binary_str, 2))
    return (divisible_index + 2) % 175 == 0