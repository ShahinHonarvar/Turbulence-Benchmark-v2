def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[91])
    missing_nums = [x for x in range(a + 1, b) if x not in nums]
    if not missing_nums:
        return ''
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].upper()
    else:
        return bin(sum_of_missing)[2:]