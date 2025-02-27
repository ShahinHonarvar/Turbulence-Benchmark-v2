def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    sum_of_missing_nums = sum((i for i in range(a + 1, b) if i not in nums[33:44]))
    if sum_of_missing_nums == 0:
        return ''
    elif sum_of_missing_nums % 2 == 0:
        return hex(sum_of_missing_nums)[2:]
    else:
        return bin(sum_of_missing_nums)[2:]