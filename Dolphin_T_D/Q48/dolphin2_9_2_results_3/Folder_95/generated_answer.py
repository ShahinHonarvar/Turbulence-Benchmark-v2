def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    missing_nums = [i for i in range(a + 1, b) if i not in nums]
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]