def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    sum_nums = sum(set(range(a + 1, b)) - set(nums[2:4]))
    if sum_nums % 2 == 0:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]