def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums[40:201]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]