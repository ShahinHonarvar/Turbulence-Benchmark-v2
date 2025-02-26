def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[36:53]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]