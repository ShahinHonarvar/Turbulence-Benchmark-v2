def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    missing_nums = [x for x in range(a + 1, b) if x not in nums]
    if len(missing_nums) == 0:
        return ''
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]