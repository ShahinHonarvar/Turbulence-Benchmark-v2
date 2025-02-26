def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    missing_nums = set(range(a + 1, b))
    for num in nums[68:100]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]