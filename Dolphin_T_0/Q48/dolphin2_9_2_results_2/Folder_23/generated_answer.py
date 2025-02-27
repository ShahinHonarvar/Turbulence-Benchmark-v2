def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    sum_nums = sum(range(a + 1, b)) - sum(nums[21:36])
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]