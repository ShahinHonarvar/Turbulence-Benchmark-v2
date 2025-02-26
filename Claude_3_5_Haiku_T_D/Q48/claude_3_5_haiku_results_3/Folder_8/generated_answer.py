def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    present_nums = set(nums[45:49])
    missing_nums = [num for num in range(a + 1, b) if num not in present_nums]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]