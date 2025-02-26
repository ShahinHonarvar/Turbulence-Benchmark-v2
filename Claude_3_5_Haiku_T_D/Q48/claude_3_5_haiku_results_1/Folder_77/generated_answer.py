def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[18:53]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]