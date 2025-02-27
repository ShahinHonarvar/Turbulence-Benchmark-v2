def return_binary_or_hexa(nums):
    a = nums[35]
    b = nums[64]
    total_sum = sum(range(a + 1, b))
    missing_nums = [x for x in range(a + 1, b) if x not in nums[36:65]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]